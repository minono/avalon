from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class EntryConsumer(WebsocketConsumer):

    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'room_{}'.format(self.room_id)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.channel_name)
        print(self.channel_name)
        print(self.channel_name)
        print(self.channel_name)
        print(self.channel_name)
        print(self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data, **kwargs):
        text_data_json = json.loads(text_data)
        player_name = text_data_json['player_name']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'player_name': player_name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        player_name = event['player_name']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'player_name': player_name
        }))
