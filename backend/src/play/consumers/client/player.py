from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from play.game.models.states import State
import json

class PlayerConsumer(WebsocketConsumer):
    def connect(self):
        self.game_token = self.scope['url_route']['kwargs']['game_token']
        self.host_group_name = 'host_%s' % self.game_token
        self.players_group_name = 'players_%s' % self.game_token

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.players_group_name,
            self.channel_name
        )

        self.accept()

        # register player's channel name with host
        self.send_to_host('connect')

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.players_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        data = text_data_json['data']

        if type == 'answer':
            print('answered')
            self.send_to_host('answer', data)
        elif type == 'registration':
            print('registered')
            self.send_to_host('registration', data)

    def send_to_host(self, type, data={}):
        async_to_sync(self.channel_layer.group_send)(
            self.host_group_name,
            {
                'channel': self.channel_name,
                'type': f'{type}_message',
                'data': data
            }
        )

    def send_to_frontend(self, state, data={}):
        self.send(text_data=json.dumps({
            'state': state,
            'data': data
        }))

    def change_state_message(self, event):
        state = event['state']
        data = event.get('data', {})

        self.send_to_frontend(state, data)