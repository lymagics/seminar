from django.urls import path

from posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
]

app_name = 'posts'
