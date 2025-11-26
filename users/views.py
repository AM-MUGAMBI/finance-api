# users/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from categories.models import Category
from categories.serializers import CategorySerializer
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

User = get_user_model()

# --------------------------------
# User Registration View
# --------------------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow users without login

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )

# --------------------------------
# List Users View
# --------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list_api(request):
    users = User.objects.all().values("id", "username", "email")
    return Response({"users": list(users)}, status=status.HTTP_200_OK)

# --------------------------------
# Retrieve User Details including Categories and Transactions
# --------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail_api(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    categories = Category.objects.filter(user=user)
    transactions = Transaction.objects.filter(user=user)

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "currency": getattr(user, "currency", "USD"),
        "categories": CategorySerializer(categories, many=True).data,
        "transactions": TransactionSerializer(transactions, many=True).data,
    })

# --------------------------------
# JWT Token Obtain View
# --------------------------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
