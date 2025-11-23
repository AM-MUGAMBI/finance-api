from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Fields to display in admin
    list_display = ('id', 'username', 'email', 'currency', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'currency')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'currency'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('id',)
    filter_horizontal = ('groups', 'user_permissions')

# Register the custom user model
admin.site.register(User, UserAdmin)
