from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from play.game.game import Game
from play.game.models.states import State
import json

class HostConsumer(WebsocketConsumer):
    def connect(self):

        def checkTeamNumber(qp):
            try:
                return int(qp['teamNumber'])
            except:
                return 0

        self.game_token = self.scope['url_route']['kwargs']['game_token']
        query_parameters = self.processQueryString(self.scope['query_string'])
        teamNumber = checkTeamNumber(query_parameters)
        self.host_group_name = 'host_%s' % self.game_token
        self.players_group_name = 'players_%s' % self.game_token
        self.game = Game(self.game_token, teamNumber)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.host_group_name,
            self.channel_name
        )

        self.accept()
        self.send_to_frontend(State.REGISTRATION, {'message': 'waiting for connections and registrations...'})

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.host_group_name,
            self.channel_name
        )
        output = self.game.deactivate()
        self.send_to_frontend(State.FINISHED, output.host['data'])
        # self.send_to_all_individual_players(State.FINISHED, output.players['data'])

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        output = self.game.change_state()
        current_state = self.game.get_state().state

        if output.has_host_data():
            self.send_to_frontend(current_state, output.host['data'])
        if output.has_group_data():
            self.send_to_group(current_state, output.group['data'])
        elif output.has_players_data():
            self.send_to_all_individual_players(current_state, output.players['data'])

    def connect_message(self, event):
        channel = event['channel']
        print(f'event: {event}')
        self.game.add_player(channel)
        print(f'connected {channel}')
        message = 'now register...'
        self.send_to_player(channel, State.REGISTRATION, {'message': message})

    def registration_message(self, event):
        channel = event['channel']
        print(f'event: {event}')
        name = event['data']
        self.game.set_player_name(channel, name)
        message = f'welcome {name}'
        self.send_to_player(channel, State.STANDBY, {'message': message})
        self.send_to_frontend(State.REGISTRATION, {'name': name})

    def answer_message(self, event):
        channel = event['channel']
        answer = event['data']
        all_answers_in = self.game.score_answer(channel, answer)
        if all_answers_in:
            self.receive(json.dumps({'message': 'done'}))
        else:
            message = 'waiting for everyone to answer...'
            self.send_to_player(channel, State.STANDBY, {'message': message})

    def send_to_player(self, channel, state, data={}, type='change_state_message'):
        async_to_sync(self.channel_layer.send)(
            channel,
            {
                'type': type,
                'state': state,
                'data': data
            }
        )

    def send_to_group(self, state, data={}, type='change_state_message'):
        async_to_sync(self.channel_layer.group_send)(
            self.players_group_name,
            {
                'type': type,
                'state': state,
                'data': data
            }
        )

    def send_to_all_individual_players(self, state, players={}, type='change_state_message'):
        for channel in players:
            self.send_to_player(channel, state, players[channel])

    def send_to_frontend(self, state, data={}):
        self.send(text_data=json.dumps({
            'state': state,
            'data': data
        }))

    def processQueryString(self, raw_query_string):
        query_parameters = {}
        query_string = raw_query_string.decode("utf-8")
        args = query_string.split('&')
        for arg in args:
            kv = arg.split('=')
            query_parameters[kv[0]] = kv[1]
        return query_parameters