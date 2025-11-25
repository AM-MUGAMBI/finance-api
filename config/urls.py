# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Optional: simple home view so / doesn't return 404
def home(request):
    return HttpResponse("Welcome to the Finance API!")

urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/transactions/', include('transactions.urls')),
]
