from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from users.models import User


class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/edit.html'
    fields = ('username', 'about_me',)

    def get_object(self):
        return self.request.user
