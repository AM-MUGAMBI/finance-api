from django.db import models
from django.conf import settings
from categories.models import Category
from django.utils import timezone  # <--- import this

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(default=timezone.now)  # <--- automatically sets today's date
    created_at = models.DateTimeField(auto_now_add=True)
    category_transaction_id = models.PositiveIntegerField(editable=False, default=0)

    def save(self, *args, **kwargs):
        if not self.category_transaction_id or self.category_transaction_id == 0:
            last = Transaction.objects.filter(user=self.user, category=self.category).order_by('category_transaction_id').last()
            self.category_transaction_id = 1 if not last else last.category_transaction_id + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} - {self.amount} (Category ID {self.category_transaction_id})"
