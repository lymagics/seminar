from hashlib import md5

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse

from model_utils import models as mu


class User(mu.TimeStampedModel,
           mu.SoftDeletableModel,
           AbstractUser):
    """
    User entity.
    """
    about_me = models.TextField(default='', blank=True)
    following = models.ManyToManyField('self',
                                       related_name='followers',
                                       symmetrical=False)
    
    def follow(self, user):
        if not self.is_following(user):
            self.following.add(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(pk=user.pk).exists()

    objects = UserManager()

    @property
    def avatar_url(self) -> str:
        avatar_hash = md5(self.email.encode()).hexdigest()
        return f'https://www.gravatar.com/avatar/{avatar_hash}?d=identicon'

    def get_absolute_url(self) -> str:
        return reverse('users:detail', kwargs={'pk': self.pk})
