import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    # Class-level dictionary to keep track of the number of players in each room
    rooms = {}

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'game_{self.room_name}'

        # Initialize room in the dictionary if it doesn't exist
        if self.room_group_name not in GameConsumer.rooms:
            GameConsumer.rooms[self.room_group_name] = 0

        # Increment the player count
        GameConsumer.rooms[self.room_group_name] += 1

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Check the number of players in the room
        if GameConsumer.rooms[self.room_group_name] == 1:
            await self.send(text_data=json.dumps({
                'message': 'Waiting for opponent...'
            }))
        elif GameConsumer.rooms[self.room_group_name] == 2:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'game_message',
                    'message': 'Opponent found!'
                }
            )

    async def disconnect(self, close_code):
        # Decrement the player count
        if self.room_group_name in GameConsumer.rooms:
            GameConsumer.rooms[self.room_group_name] -= 1
            if GameConsumer.rooms[self.room_group_name] == 0:
                del GameConsumer.rooms[self.room_group_name]

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Broadcast message to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': message
            }
        )

    # Receive message from the group
    async def game_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))