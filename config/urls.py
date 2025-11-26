# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Finance API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                color: #333;
                text-align: center;
                margin-top: 50px;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 18px;
            }
            a {
                text-decoration: none;
                color: #2196F3;
                font-weight: bold;
                margin: 0 10px;
            }
            a:hover {
                color: #0b7dda;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                margin: 10px;
            }
            .button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Finance API!</h1>
        <p>Manage your users, categories, and transactions easily.</p>
        <p>
            <a class="button" href="/api/users/register/">Sign Up</a>
            <a class="button" href="/api/users/token/">Login</a>
        </p>
        <p>Admin Panel: <a href="/admin/">Click Here</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
