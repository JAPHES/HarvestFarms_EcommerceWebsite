"""
URL configuration for HarvestFarms_EcommerceWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from cart import views
from core.views import home_view
import logging
logger = logging.getLogger(__name__)
def check_url_patterns(urlconf):
    for pattern in urlconf.url_patterns:
        logger.debug(f"Checking pattern: {pattern}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),  # Contact form
    path('', include('core.urls')),  # Home and general pages
    path('accounts/', include('accounts.urls')),  # Authentication
    path('shop/', include('shop.urls')),  # Shop products
    path('cart/', include('cart.urls')),  # Cart management
    path('login/', include('accounts.urls')),
    path('logout/', include('accounts.urls')),
    path('checkout/', views.checkout, name='checkout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
