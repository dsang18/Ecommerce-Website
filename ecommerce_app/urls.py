"""ecommer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="Home"),
    path('shop/about/', views.about, name="About"),
    path('shop/contact/', views.contact, name="Contact"),
    path('shop/track-order/', views.tracker, name="Tracker"),
    path('shop/search/', views.search, name="Search"),
    path('shop/products/<int:input_id>', views.productView, name="ProductView"),
    path('shop/checkout/', views.checkout, name="Checkout"),
    path('shop/order-placed/<int:input_id>/', views.order_placed, name="Order_placed"),
    
]
