import json

from game.models import Hook

from .hook import Hooks
from .states import GameState, State


class GameOutline:
    def __init__(self):
        self.states = []
        self.past_states = []
        self.current_state = None
        self.hooks = Hooks()
        self.hook_names_by_creator = {}

    def add_state(self, state):
        self.states.append(state)

    def add_states(self, states):
        self.states += states

    def get_current_state(self) -> GameState:
        return self.current_state

    def next_state(self) -> GameState:
        state = self.states.pop(0)
        self.past_states.append(state)
        self.current_state = state
        return state

    def previous_state(self):
        state = self.past_states.pop(len(self.past_states) - 1)
        self.states.insert(0, self.current_state)
        self.current_state = state

    def to_json_string(self):
        return json.dumps(self.states, default=lambda x: x.__dict__)

    def process_hooks(self, game_state):
        if game_state.pre_hook:
            self.hooks.add(game_state.pre_hook)
            self.hook_names_by_creator_insert(game_state.pre_hook)
        if game_state.hook:
            self.hooks.add(game_state.hook)
            self.hook_names_by_creator_insert(game_state.hook)
        if game_state.post_hook:
            self.hooks.add(game_state.post_hook)
            self.hook_names_by_creator_insert(game_state.post_hook)

    def hook_names_by_creator_insert(self, hook):
        if hook.creator_id in self.hook_names_by_creator:
            if hook.name not in self.hook_names_by_creator[hook.creator_id]:
                self.hook_names_by_creator[hook.creator_id].append(hook.name)
        else:
            self.hook_names_by_creator[hook.creator_id] = [hook.name]

    def set_hooks_code(self):
        for creator_id, hook_names in self.hook_names_by_creator.items():
            hooks_query_set = Hook.objects.filter(creator__id=creator_id, name__in = hook_names)
            for hook_model in hooks_query_set:
                self.hooks.get(creator_id, hook_model.name).code = hook_model.code

    @staticmethod
    def create_game_outline(gameOutlineString):
        game_outline = GameOutline()
        game_states_dict = json.loads(gameOutlineString)
        for state in game_states_dict:
            game_state = GameState(
                State(state['state']),
                state.get('pre_hook', None),
                state.get('post_hook', None),
                state.get('name', None)
            )
            game_outline.states.append(game_state)
            game_outline.process_hooks(game_state)
        game_outline.set_hooks_code()
        return game_outline
