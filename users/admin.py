from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from categories.models import Category
from transactions.models import Transaction

# -------------------------------
# Transaction Admin
# -------------------------------
class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    readonly_fields = ('amount', 'type', 'category', 'description', 'date', 'created_at')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'type', 'category', 'description', 'date', 'created_at')
    search_fields = ('user__username', 'category__name', 'description')
    list_filter = ('type', 'date', 'category')

# -------------------------------
# Category Admin
# -------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    search_fields = ('name', 'user__username')

# -------------------------------
# User Admin
# -------------------------------
class TransactionInlineForUser(admin.TabularInline):
    model = Transaction
    extra = 0
    readonly_fields = ('amount', 'type', 'category', 'description', 'date', 'created_at')

class CategoryInlineForUser(admin.TabularInline):
    model = Category
    extra = 0
    readonly_fields = ('name',)

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
    
    # Inline related data
    inlines = [CategoryInlineForUser, TransactionInlineForUser]

# Register the custom user model
admin.site.register(User, UserAdmin)
