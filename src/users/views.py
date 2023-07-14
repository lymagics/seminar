from django.views.generic.detail import DetailView

from users.models import User


class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'
