from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from users.forms import UserChangeForm, UserCreationForm
from users.models import User


class UserAdmin(auth_admin.UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('id', 'username', 'email',)
    fieldsets = (('Edit user', {
        'fields': (
            'email',
            'username',
            'about_me',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_removed',
        ),
    }),)
    add_fieldsets = ((None, {
        'fields': (
            'username',
            'email',
            'password1',
            'password2',
        )
    }),)


admin.site.register(User, UserAdmin)
