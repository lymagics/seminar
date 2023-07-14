from django.contrib.auth import forms as auth_forms

from users.models import User


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'about_me',
                  'created', 'modified', 'is_removed',)
