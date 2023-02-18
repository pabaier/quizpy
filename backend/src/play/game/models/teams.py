import json
import random
from math import floor


class Team():
    def __init__(self, name=''):
        self.players = []
        self.roundScore = 0
        self.totalScore = 0
        self.name = name


class Teams():
    def __init__(self, number_of_teams=2):
        self.teams = {}
        self.number_of_teams = number_of_teams

    def add(self, name, team=None) -> Team:
        if not team:
            team = Team()
        team.name = name
        self.teams[name] = team
        return team

    def get(self, name) -> Team:
        return self.teams[name]

    def get_team_keys(self):
        return list(self.teams.keys())

    def sort_by_total_score(self):
        ''' Returns list of {'totalScore': '7', 'name': 'team go'} '''

        sorted_teams = []
        for index, team_tuple_id_value in enumerate(
                sorted(self.teams.items(), key=lambda team: team[1].totalScore, reverse=True), start=1):
            team_name = team_tuple_id_value[0]
            team_total_score = self.teams[team_name].totalScore
            sorted_teams.append({
                'name': team_name,
                'totalScore': team_total_score
            })
        return sorted_teams

    def toDict(self):
        ''' returns a dict of channel keys and player object values'''
        json_string = json.dumps(self.teams, default=lambda x: x.__dict__)
        return json.loads(json_string)

    def make_teams(self, players):
        team_colors = ["Silver", "White", "Grey", "Black", "Navy", "Blue", "Cerulean", "Azure", "Turquoise", "Teal",
                       "Cyan", "Green", "Lime", "Chartreuse", "Purlple", "Yellow", "Red", "Orange", "Indego", "Violet"]
        team_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
                        "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five",
                        "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one",
                        "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven",
                        "thirty-eight", "thirty-nine", "forty", "forty-one", "forty-two", "forty-three", "forty-four",
                        "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty"]

        team_name_array = team_colors
        if random.randint(0, 1) == 0:
            team_name_array = team_numbers

        team_names = random.sample(team_name_array, self.number_of_teams)
        players_per_team = floor(len(players) / self.number_of_teams)
        players_left = players.get_player_keys()

        # assign a group of players to each team
        for name in team_names:
            team = self.add(name)
            team_players = random.sample(players_left, players_per_team)
            for channel in team_players:
                player = players.get(channel)
                team.players.append(player)
                player.team = name
                players_left.remove(channel)

        # if the teams are uneven, add each left over player to a team
        for index, channel in enumerate(players_left):
            team = self.get(team_names[index])
            player = players.get(channel)
            player.team = team.name
            team.players.append(player)

    def __iter__(self):
        ''' returns the Iterator object '''
        return TeamsIterator(self)


class TeamsIterator:
    ''' Iterator class '''

    def __init__(self, teams):
        self._teams_keys = teams.get_team_keys()
        self._teams = teams
        # member variable to keep track of current index
        self._index = 0

    def __next__(self):
        ''''Returns the next value from team object's lists '''
        if self._index < len(self._teams_keys):
            result = self._teams.get(self._teams_keys[self._index])
            self._index += 1
            return result
        # End of Iteration
        raise StopIteration
