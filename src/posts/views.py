from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from core.views import ActionView
from posts.models import Post, Like


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_queryset(self):
        return Post.objects.select_related('author')


class LikePostView(LoginRequiredMixin,
                   SingleObjectMixin,
                   ActionView):
    model = Post
    url = reverse_lazy('pages:home')

    def perform_action(self):
        post = self.get_object()
        Like.objects.get_or_create(post=post, 
                                   user=self.request.user)


class UnlikePostView(LoginRequiredMixin,
                      SingleObjectMixin,
                      ActionView):
    model = Post
    url = reverse_lazy('pages:home')

    def perform_action(self):
        post = self.get_object()
        like = Like.objects.filter(post=post, 
                                   user=self.request.user).first()
        if like is not None:
            like.delete()
