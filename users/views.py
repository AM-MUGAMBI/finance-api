from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

# ----------------------
# Render login page
# ----------------------
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # change this to your dashboard/homepage
        else:
            context = {"error": "Invalid username or password"}
            return render(request, "login.html", context)
    return render(request, "login.html")

# ----------------------
# Register new user (API)
# ----------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# ----------------------
# List all users (API, protected)
# ----------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
