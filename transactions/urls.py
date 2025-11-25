from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list_api, name='transactions_api'),
    path('create/', views.create_transaction_api, name='create_transaction_api'),
]
