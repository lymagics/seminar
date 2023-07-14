import factory
from factory.django import DjangoModelFactory

from users.tests.factories import UserFactory
from posts.models import Post


class PostFactory(DjangoModelFactory):
    text = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Post
