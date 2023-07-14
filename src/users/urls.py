from django.urls import path

from users import views

urlpatterns = [
    path('edit/', views.UserUpdateView.as_view(), name='edit'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
]

app_name = 'users'
