from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # Include only fields clients need to provide; auto fields are read-only
        fields = [
            'id', 'category', 'amount', 'type', 
            'description', 'date', 'category_transaction_id', 'created_at'
        ]
        read_only_fields = ['id', 'category_transaction_id', 'created_at']
