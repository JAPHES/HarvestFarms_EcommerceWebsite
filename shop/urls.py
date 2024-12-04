from django.urls import path
from .views import product_list, product_detail, add_product
from . import views
app_name = 'shop'
from .views import ProductDetailView


urlpatterns = [
    path('', views.product_list, name='product_list'),  # List products
    path('add/', views.add_product, name='add_product'),  # Add new product
    path('category/<slug:category_slug>/', product_list, name='category_detail'),  # Filter products by category
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),

]

