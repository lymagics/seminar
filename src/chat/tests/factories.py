import factory
from factory.django import DjangoModelFactory

from chat.models import Chat, Message
from users.tests.factories import UserFactory


class ChatFactory(DjangoModelFactory):
    initiator = factory.SubFactory(UserFactory)
    participant = factory.SubFactory(UserFactory)

    class Meta:
        model = Chat


class MessageFactory(DjangoModelFactory):
    text = factory.Faker('sentence')
    author = factory.SubFactory(UserFactory)
    chat = factory.SubFactory(ChatFactory)

    class Meta:
        model = Message
