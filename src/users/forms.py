from django import forms
from django.contrib.auth import forms as auth_forms

from users.models import User


class UserCreationForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match!')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'about_me',)
