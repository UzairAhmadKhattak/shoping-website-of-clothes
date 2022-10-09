from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index, name='home'),
    path('products', views.product),
    path('about', views.about_us),
    path('contact', views.contact_us),
]
