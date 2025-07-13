from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    history = HistoricalRecords()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    history = HistoricalRecords()

