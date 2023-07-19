from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('chat/', include('chat.urls')),
    path('', include('pages.urls')),
]
