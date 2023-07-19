import uuid

from django.conf import settings
from django.db import models


class Chat(models.Model):
    """
    Chat entity.
    """
    ref = models.UUIDField(default=uuid.uuid4)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='chats')

    def __str__(self) -> str:
        return str(self.ref)


class Message(models.Model):
    """
    Message entity.
    """
    text = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='messages')
    chat = models.ForeignKey(Chat,
                             on_delete=models.CASCADE,
                             related_name='messages')

    def __str__(self) -> str:
        return self.text[:50]
