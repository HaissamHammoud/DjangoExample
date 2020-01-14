from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('product/detail/<int:my_id>',views.product_dynamic_view, name= 'detail'),
    path('menu', views.loja_view,name = 'menu'),
    path('product/create/', views.product_create_view, name = 'Create'),
    path('product/top_products/',views.top_products, name = 'top'),

]
