from django.shortcuts import get_object_or_404

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.models import Chat, Message
from users.models import User


@database_sync_to_async
def get_chat(ref: str):
    return get_object_or_404(Chat, ref=ref)


@database_sync_to_async
def add_message(
    text: str, author: User, chat: Chat
):
    Message.objects.create(text=text,
                           author=author,
                           chat=chat)


@database_sync_to_async
def is_participant(
    user: User, chat: Chat
) -> bool:
    return chat.initiator == user or \
        chat.participant == user


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """
    Consumer to serve chat messages.
    """
    async def connect(self):
        self.ref = self.scope['url_route']['kwargs']['ref']
        self.chat = await get_chat(self.ref)
        if not await is_participant(self.scope['user'], self.chat):
            return await self.close()
        await self.channel_layer.group_add(self.ref, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.ref, self.channel_name)

    async def receive_json(self, content):
        message = content.get('message')
        await add_message(message, self.scope['user'], self.chat)
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
