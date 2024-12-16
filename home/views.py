from django.shortcuts import render, redirect
# from .forms import ProductForm

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')  # Redirect to the product list page
#     else:
#         form = ProductForm()
#     return render(request, 'home/add_product.html', {'form': form})

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def gallery(request):
    return render(request, 'home/gallery.html') 

def about(request):
    return render(request, 'home/about.html')

def shop_now(request):
    return render(request, 'home/shop_now.html')

def track_order(requset):
    return render(requset, 'home/track_order.html')

def blog(requset):
    return render(requset, 'home/blog.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart.items.all())
    return render(request, 'home/cart.html', {
        'cart': cart,
        'total_price': total_price,
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')
