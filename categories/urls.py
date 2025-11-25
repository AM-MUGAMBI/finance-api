from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_api, name='categories_api'),
    path('create/', views.create_category_api, name='create_category_api'),
]
