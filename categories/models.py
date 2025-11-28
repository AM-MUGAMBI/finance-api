from django.db import models
from django.conf import settings

class Category(models.Model):
    CATEGORY_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPES)
    color = models.CharField(max_length=7, default="#000000")
    user_category_id = models.PositiveIntegerField(editable=False, default=0)  # Default for existing rows
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.user_category_id or self.user_category_id == 0:
            # Assign the next available ID per user
            last = Category.objects.filter(user=self.user).order_by('user_category_id').last()
            self.user_category_id = 1 if not last else last.user_category_id + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.type}) - ID {self.user_category_id}"
