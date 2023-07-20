from django.conf import settings
from django.db import models

from model_utils import models as mu


class Post(mu.TimeStampedModel,
           models.Model):
    """
    Post entity.
    """
    text = models.CharField(max_length=180)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='posts')

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.text


class Like(models.Model):
    """
    Like entity.
    """
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='likes')
    
    def __str__(self) -> str:
        return f'Like of {self.post} by {self.user}'
