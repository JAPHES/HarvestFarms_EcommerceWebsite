
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product  # Assuming Product model is in 'shop'
from django.http import HttpResponse
from .models import Cart
from django.contrib.auth.decorators import login_required


# Helper function to get the cart from session
def get_cart(request):
    cart = request.session.get('cart', {})
    return cart


# Helper function to update the cart in the session
def update_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True


# View to display the cart
def cart_view(request):
    cart = request.session.get('cart', {})  # Get the cart from session, or an empty dictionary if it doesn't exist
    cart_items = []
    cart_total = 0
    total_items = 0

    # Fetch product details for each item in the cart
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        line_total = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': line_total
        })
        cart_total += line_total
        total_items += quantity

    return render(request, 'cart/view_cart.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'total_items': total_items,
    })


# View to add a product to the cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # Get the cart from session or create a new one
    cart = request.session.get('cart', {})

    # Update cart with the new item
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    # Save the cart back to session
    request.session['cart'] = cart
    request.session.modified = True

    # Redirect to the view_cart page
    return redirect('cart:view_cart')


# View to remove a product from the cart
def remove_from_cart(request, product_id):
    cart = get_cart(request)
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
    update_cart(request, cart)

    return redirect('cart:view_cart')  # Redirect to view cart page


# View to update product quantity in the cart
def update_cart_quantity(request, product_id):
    cart = get_cart(request)
    product_id = str(product_id)
    quantity = int(request.POST.get('quantity', 1))

    if product_id in cart:
        if quantity > 0:
            cart[product_id] = quantity
        else:
            del cart[product_id]

    update_cart(request, cart)
    return redirect('cart:view_cart')

@login_required
def checkout(request):
    # Get the current user's cart items
    cart_items = Cart.objects.filter(user=request.user)

    # Calculate the total price
    # Add total price calculation in the view
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    total_price = sum(item.total_price for item in cart_items)

    if request.method == 'POST':
        # Handle checkout logic (e.g., process payment, clear cart, etc.)
        cart_items.delete()  # Clear the cart after checkout
        return redirect('shop:product_list')  # Redirect to the product list or a success page

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/checkout.html', context)
