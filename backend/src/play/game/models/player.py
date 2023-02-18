import json

from .round_result import RoundResult


class Player():
    def __init__(self):
        self.channel = ''
        self.name = ''
        self.team = ''
        self.totalScore = 0
        self.rank = 0
        self.roundResult = RoundResult()


class Players():
    def __init__(self):
        self.players = {}

    def add(self, channel, player=None):
        if not player:
            player = Player()
        player.channel = channel
        self.players[channel] = player

    def get(self, channel):
        return self.players[channel]

    def __iter__(self):
        ''' returns the Iterator object '''
        return PlayersIterator(self)

    def __len__(self):
        return len(self.players)

    def sort_by_total_score(self):
        ''' Returns list of {'totalScore': '7', 'name': 'wendy'} '''

        sorted_players = []
        for index, player_tuple_id_value in enumerate(
                sorted(self.players.items(), key=lambda player: player[1].totalScore, reverse=True), start=1):
            self.players[player_tuple_id_value[0]].rank = index
            sorted_players.append({
                'name': self.players[player_tuple_id_value[0]].name,
                'totalScore': self.players[player_tuple_id_value[0]].totalScore
            })
        return sorted_players

    def get_player_keys(self):
        return list(self.players.keys())

    def toDict(self):
        ''' returns a dict of channel keys and player object values'''
        json_string = json.dumps(self.players, default=lambda x: x.__dict__)
        return json.loads(json_string)


class PlayersIterator:
    ''' Iterator class '''

    def __init__(self, players):
        self._players_keys = players.get_player_keys()
        self._players = players
        # member variable to keep track of current index
        self._index = 0

    def __next__(self):
        ''''Returns the next value from team object's lists '''
        if self._index < len(self._players_keys):
            result = self._players.get(self._players_keys[self._index])
            self._index += 1
            return result
        # End of Iteration
        raise StopIteration
