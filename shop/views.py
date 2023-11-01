from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from decimal import Decimal

from .models import Customer, Product, Cart, CartItem
from .forms import CreateUserForm

def get_cart_and_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cart_items = cart.total_quantity
    else:
        try:
            order = json.loads(request.COOKIES['cart'])
        except KeyError:
            order = {} 
        
        items = []
        cart = {'total_without_tax': 0, 'tax': 0, 'total_with_tax': 0, 'total_quantity': 0}
        cart_items = cart['total_quantity']
        
        for i in order:
            cart_items += order[i]['quantity']

            product = Product.objects.get(id=i)
            total = product.price * order[i]['quantity']
            subtotal = product.price * order[i]['quantity']
            tax = round(total * Decimal(0.2), 2)
            total_with_tax = total + tax

            cart['total_without_tax'] += total
            cart['total_with_tax'] += total_with_tax
            cart['tax'] += tax
            cart['total_quantity'] += order[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'title': product.title,
                    'description': product.description,
                    'price': product.price,
                    'image': product.image,
                },
                'subtotal': subtotal,
                'quantity': order[i]['quantity'],
                'total_without_tax': total,
                'tax': tax,
                'total_with_tax': total_with_tax
            }
            items.append(item)

    return items, cart

def products(request):
    products = Product.objects.all()
    
    items, cart = get_cart_and_items(request)

    context = {'products': products, 'cart': cart}

    return render(request, 'products.html', context)
    
def cart(request):
    items,cart = get_cart_and_items(request)

    context = {'items': items, 'cart': cart}

    return render(request, 'cart.html', context)

def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    cart, created = Cart.objects.get_or_create(customer=customer)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.prefetch_related('product').create(quantity=0, cart=cart, product=product)

    if action == 'add':
        cart_item.quantity = cart_item.quantity + 1
    elif action == 'delete':
        cart_item.quantity = cart_item.quantity - 1
    elif action == 'remove':
        cart_item.quantity = 0

    cart_item.save()

    if cart_item.quantity <= 0:
        cart_item.delete()
    
    return JsonResponse('Item was added', safe=False)

def homepage(request):
    five_products = Product.objects.all()[:5]

    items, cart = get_cart_and_items(request)

    context = {'products': five_products, 'items': items, 'cart': cart}
    return render(request, 'homepage.html', context)

@csrf_exempt
def login_page(request):

    items, cart = get_cart_and_items(request)

    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.info(request, 'Username or password is incorrect')

    context = {'cart': cart}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('login')

@csrf_exempt
def signup(request):
    form = CreateUserForm()
    items, cart = get_cart_and_items(request)

    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                Customer.objects.create(user=user)
                current_user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + current_user)
                return redirect('login')
    
    context = {'form': form, 'cart': cart}
    return render(request, 'signup.html', context)

@csrf_exempt
@login_required(login_url='login')
def profile(request):
    items, cart = get_cart_and_items(request)

    context = {'cart': cart}
    return render(request, 'profile.html', context)



    


        

