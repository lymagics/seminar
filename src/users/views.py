from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import UpdateView

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
                     RedirectView):
    model = User

    def get(self, request: HttpRequest, *args, **kwargs):
        user = self.get_object()
        request.user.follow(user)
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        user = self.get_object()
        return user.get_absolute_url()


class UnFollowUserView(LoginRequiredMixin,
                       SingleObjectMixin,
                       RedirectView):
    model = User

    def get(self, request: HttpRequest, *args, **kwargs):
        user = self.get_object()
        request.user.unfollow(user)
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        user = self.get_object()
        return user.get_absolute_url()
