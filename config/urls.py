from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # FRONTEND PAGES
    path('', views.login_page, name='login'),  # login page
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('create-transaction/', views.create_transaction_page, name='create_transaction'),
    path('transactions/', views.transactions_page, name='transactions'),
    path('categories/', views.categories_page, name='categories'),
    path('create-category/', views.create_category_page, name='create_category'),
    path('profile/', views.profile_page, name='profile'),

    # API ROUTES
    path('auth/', include('users.urls')),                  # login, register, etc.
    path('api/categories/', include('categories.urls')),  # API for categories
    path('api/transactions/', include('transactions.urls')),  # API for transactions
]
