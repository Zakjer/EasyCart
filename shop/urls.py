from django.urls import path

from shop import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('update_cart', views.update_cart, name='update_cart'),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]





