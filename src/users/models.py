from hashlib import md5

from django.contrib.auth.models import AbstractUser
from django.db import models

from model_utils import models as mu


class User(mu.TimeStampedModel,
           mu.SoftDeletableModel,
           AbstractUser):
    """
    User entity.
    """
    about_me = models.TextField(default='')

    @property
    def avatar_url(self) -> str:
        avatar_hash = md5(self.email.encode()).hexdigest()
        return f'https://www.gravatar.com/avatar/{avatar_hash}?d=identicon'
