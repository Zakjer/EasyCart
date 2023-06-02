from rest_framework import serializers
from django.db import transaction

from .models import Customer, Order, Product, ProductImage, OrderItem

class ProductImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'images']


class SimpleProductSerializer(serializers.ModelSerializer):
    """Contains only the most important informations about product"""
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone', 'birth_date']


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_item_price = serializers.SerializerMethodField(method_name='get_total_price')

    def get_total_price(self, orderitem):
        return orderitem.quantity * orderitem.product.price

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'total_item_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='calculate_total_order_price')

    def calculate_total_order_price(self, order):
        return sum([item.quantity * item.product.price for item in order.items.all()])

    class Meta:
        model = Order
        fields = ['id', 'placed_at', 'customer', 'items', 'total_price']

    





