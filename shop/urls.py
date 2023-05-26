from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('carts/', views.carts),
    path('customers/', views.customers),
    path('orders/', views.orders)
]
