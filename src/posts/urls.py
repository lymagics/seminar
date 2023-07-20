from django.urls import path

from posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('likes/', views.LikedPostsView.as_view(), name='likes'),
    path('<int:pk>/like/', views.LikePostView.as_view(), name='like'),
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike'),
]

app_name = 'posts'
