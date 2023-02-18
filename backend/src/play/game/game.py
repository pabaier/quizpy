import time
from math import ceil

from game.models import ActiveGame
from question.models import QuestionGame, QuestionAnswerOption

from .models.game_outline import GameOutline
from .models.output import Output
from .models.player import Players
from .models.round_result import RoundResult
from .models.states import State, GameState
from .models.teams import Teams


class Game:
    def __init__(self, game_token, number_of_teams):
        self.isTeam = number_of_teams > 0
        self.active_game = None
        self.questions, self.answers, self.individual_scoring_hook, self.team_scoring_hook = self.get_game(game_token)

        self.players = Players()
        self.teams = Teams(number_of_teams)

        self.outline = self.get_outline(self.active_game.game.outline)

        self.output = Output()
        self.start_time = None
        self.calculate_individual_score = self.set_individual_scoring_function()
        self.calculate_team_score = self.set_team_scoring_function()
        self.number_of_answers = 0
        self.custom_individual_scoring_return = 0
        self.answering_question = False

    def set_team_scoring_function(self):
        if self.team_scoring_hook:
            return self.custom_team_scoring
        return self.default_team_scoring

    def custom_team_scoring(self):
        exec(self.team_scoring_hook)

    def default_team_scoring(self):
        for team in self.teams:
            for player in team.players:
                score = player.roundResult.score
                team.totalScore += score
                team.roundScore += score

    def set_individual_scoring_function(self):
        if self.individual_scoring_hook:
            return self.custom_individual_scoring
        return self.default_individual_scoring

    def custom_individual_scoring(self, result, channel):
        exec(self.individual_scoring_hook, {'results': result, 'channel': channel, 'self': self})
        return self.custom_individual_scoring_return

    def default_individual_scoring(self, result, channel):
        time = self.get_question()['time']
        score = ceil((time - result.time) / time * 1000)
        if score < 100:
            score = 100
        return score

    def get_outline(self, outline_string) -> GameOutline:
        outline = GameOutline.create_game_outline(outline_string)
        return outline

    # [{id, text, time, answers[option, option,...]},...], [['yes'], ['hi', 'ho'],...]
    def get_game(self, game_token):
        self.active_game = ActiveGame.objects.get(slug=game_token)
        qg = QuestionGame.objects.all().select_related('game', 'question').filter(game=self.active_game.game)

        individual_scoring_hook = None
        team_scoring_hook = None
        questions = []
        answers = []

        team_scoring = qg.first().game.team_scoring_hook
        if team_scoring:
            team_scoring_hook = team_scoring.code
        individual_scoring = qg.first().game.individual_scoring_hook
        if individual_scoring:
            individual_scoring_hook = individual_scoring.code

        for e in qg:
            answerOptions = QuestionAnswerOption.objects.all().select_related('question').filter(question=e.question)
            question = {
                'id': e.question.id,
                'text': e.question.text,
                'time': e.time_limit
            }
            answerOptionList = []
            answer = []
            for a in answerOptions:
                answerOptionList.append(a.option)
                if a.isAnswer:
                    answer.append(a.option)
            question['answers'] = answerOptionList
            answers.append(answer)
            questions.append(question)
        return questions, answers, individual_scoring_hook, team_scoring_hook,

    def check_answer(self, answer):
        return answer in self.answers[0]

    def next_question(self):
        if len(self.questions) > 0:
            self.answers.pop(0)
            self.questions.pop(0)
            return self.get_question()

    def get_question(self):
        if len(self.questions) == 0:
            return None
        return self.questions[0]

    def get_state(self) -> GameState:
        return self.outline.get_current_state()

    def set_teams(self, set_teams_lambda):
        set_teams_lambda(self)

    def add_player(self, channel):
        self.players.add(channel)

    def set_player_name(self, channel, name):
        player = self.players.get(channel)
        self.players.get(channel).name = name

    def deactivate(self):
        self.active_game.delete()
        self.output.host['data'] = self.generate_leaderboard()
        self.output.players['data'] = self.players.toDict()
        self.output.group['data'] = None
        self.outline = GameOutline()
        self.questions = self.answers = []
        return self.output

    def get_results(self):
        return self.generate_leaderboard()

    def score_answer(self, channel, answer):
        player = self.players.get(channel)
        time_taken = time.time() - self.start_time
        correct = self.check_answer(answer)
        score = 0
        round_result = RoundResult(answer=answer, correct=correct, time=time_taken)
        if correct:
            score = self.calculate_individual_score(round_result, channel)
            round_result.score = score
        player.roundResult = round_result
        player.totalScore += score
        self.number_of_answers += 1
        all_in = self.all_answers_in()
        if all_in:
            self.number_of_answers = 0
        return all_in

    def all_answers_in(self):
        return len(self.players) == self.number_of_answers

    def reset_round_results(self):
        for player in self.players:
            player.roundResults = RoundResult()
        for team in self.teams:
            team.roundScore = 0

    def generate_leaderboard(self):

        sorted_players = self.players.sort_by_total_score()

        if self.isTeam:
            return self.teams.sort_by_total_score()

        return sorted_players

    def execute_hook(self, code):
        exec(code)

    def change_state(self):
        gameState = self.outline.next_state()
        state = gameState.state
        self.output.reset()
        if self.answering_question:
            self.answering_question = False
            self.next_question()

        if gameState.pre_hook:
            print('pre hook')
            self.execute_hook(self.outline.hooks.get(gameState.pre_hook.creator_id, gameState.pre_hook.name).code)

        if state is State.HOOK:
            print('hook method')
            self.execute_hook(self.outline.hooks.get(gameState.hook.creator_id, gameState.hook.name).code)
        elif state is State.MAKE_TEAMS:
            print('make teams method')
            if self.isTeam:
                self.teams.make_teams(self.players)
                self.output.host['data'] = self.teams.toDict()
                self.output.players['data'] = self.players.toDict()
        elif state is State.QUESTION:
            print('asking question...')
            self.answering_question = True
            self.output.host['data'] = self.output.group['data'] = self.get_question()
            self.reset_round_results()
            self.start_time = time.time()
        elif state is State.LEADERBOARD:
            print('leaderboard method')
            if self.isTeam:
                self.calculate_team_score()
            self.output.host['data'] = self.generate_leaderboard()
            self.output.players['data'] = self.players.toDict()
        elif state is State.FINISHED:
            print('calculating results')
            self.output.host['data'] = self.generate_leaderboard()
            self.output.players['data'] = self.players.toDict()
        else:
            print('passing')

        if gameState.post_hook:
            print('post hook')
            self.execute_hook(self.outline.hooks.get(gameState.post_hook.creator_id, gameState.post_hook.name).code)

        if self.output.has_something_to_send():
            return self.output
        return self.change_state()
