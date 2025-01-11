

from datetime import datetime
from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    createdAt = models.DateField(default=datetime.now)
    inStock = models.BooleanField(default=False)
    description = models.TextField(null=True)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title
