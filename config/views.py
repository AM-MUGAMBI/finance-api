from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

@api_view(['POST'])
def signup_api(request):
    # handle signup logic
    return Response({"message": "User created successfully"})

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return Response({"message": "Login successful"})
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def logout_api(request):
    logout(request)
    return Response({"message": "Logged out successfully"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_api(request):
    return Response({"message": f"Welcome {request.user.username}!"})
