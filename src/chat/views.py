from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.views.generic.detail import DetailView
from django.shortcuts import redirect

from chat.models import Chat
from users.models import User


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        me = self.request.user
        user = self.get_object()
        chat = me.chats.filter(users__in=[user]).first()
        if chat is None:
            chat = Chat.objects.create()
            chat.users.add(me)
            chat.users.add(user)
        context['chat'] = chat
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs):
        user = self.get_object()
        if self.request.user == user:
            return redirect(user.get_absolute_url())
        return super().get(request, *args, **kwargs)
