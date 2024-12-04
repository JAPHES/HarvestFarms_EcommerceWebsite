from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('view/', views.cart_view, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add product to cart
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove product from cart
    path('update/<int:product_id>/', views.update_cart_quantity, name='update_cart_quantity'),  # Update product quantity in cart
    path('', views.cart_view, name='cart'),  # View the cart (can be added to view the entire cart)
    #path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('view/', views.cart_view, name='view_cart'),
    #path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    #path('checkout/', views.checkout, name='checkout'),  # Add this line

]
