from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse  # Helps resolve URL names to actual paths

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully!')
            return redirect('shop:product_list')

    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect("")  # Ensure "home" corresponds to a valid URL name
            return redirect('shop:product_list')  # Make sure the redirect is correctly to the products page

        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')
@login_required
def home_view(request):
    return render(request, 'shop/product_list')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect("accounts:login")  # Ensure "login" corresponds to a valid URL name

