from django.urls import path
from . import views
app_name = 'contact'

urlpatterns = [
    path('', views.contact_form_view, name='contact_form'),  # Match the `contact/` path
    path('success/', views.success_view, name='success'),
    ]


