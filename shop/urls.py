from rest_framework_nested import routers

from .views import CustomerViewSet, OrderViewSet, ProductImageViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images', ProductImageViewSet, basename='product-images')

urlpatterns = router.urls + products_router.urls



