from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shop import views
#from .views import CustomerViewSet, OrderViewSet, ProductImageViewSet, ProductViewSet, ReviewViewSet

# router = routers.DefaultRouter()
# router.register('products', ProductViewSet)
# router.register('customers', CustomerViewSet)
# router.register('orders', OrderViewSet, basename='orders')

# products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
# products_router.register('images', ProductImageViewSet, basename='product-images')
# products_router.register('reviews', ReviewViewSet, basename='product-reviews')

# urlpatterns = router.urls + products_router.urls
urlpatterns = [
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]





