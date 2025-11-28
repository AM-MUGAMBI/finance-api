from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_api, name='category-list'),             # GET all categories
    path('create/', views.create_category_api, name='category-create'),  # POST new category
    path('<int:pk>/', views.category_detail_api, name='category-detail'), # GET/PUT/DELETE specific category
]
