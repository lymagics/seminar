from django.urls import path

from users import views

urlpatterns = [
    path('edit/', views.UserUpdateView.as_view(), name='edit'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('<int:pk>/follow/', views.FollowUserView.as_view(), name='follow'),
    path('<int:pk>/unfollow/', views.UnFollowUserView.as_view(), name='unfollow'),
]

app_name = 'users'
