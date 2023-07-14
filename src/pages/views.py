from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView

from posts.forms import PostForm


class HomePageGET(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context


class HomePagePOST(CreateView):
    form_class = PostForm
    template_name = 'home.html'
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HomePageView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, *args, **kwargs):
        view = HomePageGET.as_view()
        return view(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        view = HomePagePOST.as_view()
        return view(request, *args, **kwargs)
