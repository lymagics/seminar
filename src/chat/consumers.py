from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """
    Consumer to serve chat messages.
    """
    async def connect(self):
        self.ref = self.scope['url_route']['kwargs']['ref']
        await self.channel_layer.group_add(self.ref, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.ref, self.channel_name)

    async def receive_json(self, content):
        message = content.get('message')
        await self.channel_layer.group_send(self.ref, {
            'type': 'chat.message', 
            'message': message,
            'author': self.scope['user'].username,
        })

    async def chat_message(self, event):
        await self.send_json(content={
            'message': event.get('message'),
            'author': event.get('author'),
        })
