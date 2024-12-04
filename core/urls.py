
from django.urls import path
from .views import home_view


urlpatterns = [
    path('', home_view, name='home'),  # Maps the root URL to the home_view

]

