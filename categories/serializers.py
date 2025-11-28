from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # Include only fields clients need to provide; auto fields are read-only
        fields = ['id', 'name', 'type', 'color', 'user_category_id', 'created_at']
        read_only_fields = ['id', 'user_category_id', 'created_at']
