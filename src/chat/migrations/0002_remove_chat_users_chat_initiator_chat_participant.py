# Generated by Django 4.2.3 on 2023-07-20 06:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='users',
        ),
        migrations.AddField(
            model_name='chat',
            name='initiator',
            field=models.ManyToManyField(related_name='initiated_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='participant',
            field=models.ManyToManyField(related_name='participated_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
