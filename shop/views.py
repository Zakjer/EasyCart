from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import CustomerSerializer, OrderSerializer, ProductImageSerializer, ProductSerializer, ReviewSerializer
from .models import Customer, Order, Product, ProductImage, Review
from .permissions import IsAdminOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAdminOrReadOnly]


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.prefetch_related('items__product').all()
    http_method_names = ['get', 'post', 'patch', 'head', 'options']
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    http_method_names = ['get', 'post', 'head', 'options']
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    


        

