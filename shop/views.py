from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home')

def products(request):
    return HttpResponse('products')

def carts(request):
    return HttpResponse('cart')

def customers(request):
    return HttpResponse('customers')

def orders(request):
    return HttpResponse('orders')