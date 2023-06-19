from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from django.shortcuts import render

from .serializers import CustomerSerializer, OrderSerializer, ProductSerializer, ReviewSerializer
from .models import Customer, Order, Product, Review, OrderItem, Cart
from .permissions import IsAdminOrReadOnly


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)
    
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
    else:
        items = []

    context = {'items': items, 'cart': cart}

    return render(request, 'cart.html', context)

def homepage(request):
    five_products = Product.objects.all()[:5]
    context = {
        'products': five_products
    }
    return render(request, 'homepage.html', context)

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.prefetch_related('images').all()
#     serializer_class = ProductSerializer
#     permission_classes=[IsAdminOrReadOnly]
#     renderer_classes = [TemplateHTMLRenderer]

#     def get(self, request):
#         queryset = Product.objects.prefetch_related('images').all()
#         return Response({'products': queryset})

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, 
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)

#         return super().destroy(request, *args, **kwargs)


# class ProductImageViewSet(ModelViewSet):
#     serializer_class = ProductImageSerializer
#     permission_classes = [IsAdminOrReadOnly]
    
#     def get_queryset(self):
#         return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
    
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}
    

# class CustomerViewSet(ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [IsAdminUser]


# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.prefetch_related('items__product').all()
#     http_method_names = ['get', 'post', 'patch', 'head', 'options']
#     serializer_class = OrderSerializer
#     permission_classes = [IsAdminUser]
    

# class ReviewViewSet(ModelViewSet):
#     http_method_names = ['get', 'post', 'head', 'options', 'delete']
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])

#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}
    


        

