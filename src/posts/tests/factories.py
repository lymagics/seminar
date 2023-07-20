import factory
from factory.django import DjangoModelFactory

from posts.models import Post, Like
from users.tests.factories import UserFactory


class PostFactory(DjangoModelFactory):
    text = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Post


class LikeFactory(DjangoModelFactory):
    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Like
