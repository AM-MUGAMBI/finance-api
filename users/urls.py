from django.urls import path
from .views import RegisterView, user_list

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # registration
    path('list/', user_list, name='user_list'),                 # protected user list
]
