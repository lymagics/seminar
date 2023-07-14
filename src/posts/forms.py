from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        labels = {
            'text': '',
        }
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'What is on your mind?',
            }),
        }
