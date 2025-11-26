from rest_framework import serializers
from django.contrib.auth import get_user_model
from categories.serializers import CategorySerializer
from categories.models import Category
from transactions.serializers import TransactionSerializer
from transactions.models import Transaction

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'currency')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            currency=validated_data.get('currency', 'USD')
        )
        return user

# Serializer to list users with basic info
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'currency')

# Serializer to show user details including categories & transactions
class UserDetailSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    transactions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'currency', 'categories', 'transactions')

    def get_categories(self, obj):
        categories = Category.objects.filter(user=obj)
        return CategorySerializer(categories, many=True).data

    def get_transactions(self, obj):
        transactions = Transaction.objects.filter(user=obj)
        return TransactionSerializer(transactions, many=True).data
