"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from pages.views import home
from products.views import product_dynamic_view , product_create_view, top_products, loja_view
from JogoMemoria.views import memoria_view
from estacionamento.views import *
urlpatterns = [
    path('', home ,name = "home"),
    path('admin/', admin.site.urls),

    path('loja/product/detail/<int:my_id>',product_dynamic_view),
    path('loja/menu', loja_view,name = 'menu'),
    path('loja/product/create/', product_create_view, name = 'Create'),
    path('loja/product/top_products/',top_products, name = 'Create'),
    path('memoria/',memoria_view, name = 'jogo'),
    path('estacionamento/', include('estacionamento.urls')),

]
