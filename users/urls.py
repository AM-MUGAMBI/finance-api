# users/urls.py

from django.urls import path
from .views import RegisterView, user_list_api

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', user_list_api, name='user_list_api'),
]
