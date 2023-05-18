from django.db import models
from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField()
    session_id = models.CharField(max_length=40)

class Questions(models.Model):
    username = models.CharField(max_length=150, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
