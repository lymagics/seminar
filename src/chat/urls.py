from django.urls import path

from chat.views import ChatDetailView

urlpatterns = [
    path('<int:pk>/', ChatDetailView.as_view(), name='room'),
]

app_name = 'chat'
