from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import UpdateView

from core.views import ActionView
from users.forms import UserForm
from users.models import User


class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    template_name = 'users/edit.html'

    def get_object(self):
        return self.request.user


class FollowUserView(LoginRequiredMixin,
                     SingleObjectMixin,
                     ActionView):
    model = User

    def perform_action(self):
        user = self.get_object()
        self.request.user.follow(user)

    def get_redirect_url(self, *args, **kwargs):
        user = self.get_object()
        return user.get_absolute_url()


class UnFollowUserView(LoginRequiredMixin,
                       SingleObjectMixin,
                       ActionView):
    model = User

    def perform_action(self):
        user = self.get_object()
        self.request.user.unfollow(user)

    def get_redirect_url(self, *args, **kwargs):
        user = self.get_object()
        return user.get_absolute_url()
