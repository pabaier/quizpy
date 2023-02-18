from enum import Enum

from .hook import Hook


class State(str, Enum):
    HOOK = 'hook'
    REGISTRATION = 'registration'
    MAKE_TEAMS = 'makeTeams'
    QUESTION = 'question'
    STANDBY = 'standby'
    LEADERBOARD = 'leaderboard'
    FINISHED = 'finished'
    GAME_OVER = 'gameOver'


class GameState:
    def __init__(self, state, pre_hook_name=None, post_hook_name=None, hook_name=None):
        self.pre_hook = self.proccess_hook_name(pre_hook_name)
        self.state = state
        self.hook = self.proccess_hook_name(hook_name)
        self.post_hook = self.proccess_hook_name(post_hook_name)

    def proccess_hook_name(self, hook_name) -> Hook:
        if not hook_name: return None
        parts = hook_name.split('.')
        if len(parts) is 2:
            return Hook(parts[1], parts[0])
        return Hook(parts[0])
