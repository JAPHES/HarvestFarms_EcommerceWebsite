from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.views.generic import DetailView

# Product List View
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


# Product Detail View
def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })


# Add Product View
def is_superuser(user):
    return user.is_superuser


@login_required
#@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to view this page.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')  # Replace with your product list URL name
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'  # Specify your template file
    context_object_name = 'product'