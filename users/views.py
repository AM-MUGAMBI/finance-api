# users/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Class-based view for user registration
class RegisterView(APIView):
    def post(self, request):
        # Replace this with real registration logic
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

# Function-based view to list users
def user_list_api(request):
    # Replace this with real user list logic
    return Response({"users": []}, status=status.HTTP_200_OK)
