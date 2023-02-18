class Output:
    def __init__(self):
        self.reset()

    def reset(self):
        self.players = {'data': None}
        self.group = {'data': None}
        self.host = {'data': None, 'timer': None}

    def has_host_data(self):
        return self.host['data'] and True

    def has_group_data(self):
        return self.group['data'] and True

    def has_players_data(self):
        return self.players['data'] and True

    def has_something_to_send(self) -> bool:
        return self.has_group_data() or self.has_host_data() or self.has_players_data()
