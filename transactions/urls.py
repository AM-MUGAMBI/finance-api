from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list_api, name='transaction-list'),             # GET all transactions
    path('create/', views.create_transaction_api, name='transaction-create'),  # POST new transaction
    path('<int:pk>/', views.transaction_detail_api, name='transaction-detail'), # GET/PUT/DELETE specific transaction
]
