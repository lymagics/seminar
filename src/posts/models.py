from django.conf import settings
from django.db import models
from django.urls import reverse

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
    
    def __str__(self) -> str:
        return self.text
    
    def get_absolute_url(self) -> str:
        return reverse('posts:detail', kwargs={'pk': self.pk})
