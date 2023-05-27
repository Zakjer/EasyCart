from uuid import uuid4
from .validators import validate_image_size

from django.db import models
from django.core.validators import MinValueValidator


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_ordering(self):
        return None, "asc"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])


class ProductImage(models.Model):
    image = models.ImageField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, validators=[validate_image_size])


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    """Model for specific item in order"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)  
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    """Model for specific item in cart"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()



