from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView

from core.views import ActionView
from posts.models import Like, Post


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

    def get_redirect_url(self, *args, **kwargs):
        next = self.request.GET.get('next', None)
        return (next if next is not None
                else super().get_redirect_url(*args, **kwargs))


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

    def get_redirect_url(self, *args, **kwargs):
        next = self.request.GET.get('next', None)
        return (next if next is not None
                else super().get_redirect_url(*args, **kwargs))


class LikedPostsView(LoginRequiredMixin,
                     ListView):
    model = Post
    template_name = 'posts/likes.html'

    def get_queryset(self):
        return self.request.user.likes.select_related('user')
