# Generated by Django 4.2.3 on 2023-07-20 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_remove_chat_users_chat_initiator_chat_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='initiator',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='participant',
        ),
        migrations.AddField(
            model_name='chat',
            name='initiator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='initiated_chats', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='participant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='participated_chats', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]