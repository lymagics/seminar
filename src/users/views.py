from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
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
