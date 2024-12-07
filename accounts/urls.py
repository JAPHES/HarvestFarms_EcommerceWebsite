from django.urls import path,include

from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'


urlpatterns = [
    path('register/', views.register_view, name='register'),  # URL for registration
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.register_view, name='register'),

    path('home/', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),


]