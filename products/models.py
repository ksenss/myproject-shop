

from datetime import datetime
from django.db import models

class Product(models.Model):
    title= models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    createdAt = models.DateField(default=datetime.now)
    inStock = models.BooleanField(default=False)
    description = models.TextField(null=True)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title
class Cart(models.Model):
    session_id = models.CharField(max_length=255)  # Обов'язкове поле
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Прив'язка до продукту
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for session {self.session_id}"
