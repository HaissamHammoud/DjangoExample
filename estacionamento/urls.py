from django.urls import path
from . import views

app_name = 'estacionamento'
urlpatterns = [
    path('entrance/', views.car_entrance, name = "entrada"),
    path('exit/', views.car_exit, name = "saida"),
    path('',views.car_menu, name='menu'),
    path('result/detail/<int:my_id>',views.car_detail_view, name= 'car_detail'),
    path('result/<int:my_id>', views.car_redirect, name = 'redirect'),
    path('pagamento/<int:my_id>', views.pagamento, name = 'pagamento'),
    path('pagamento/confirmado/<int:my_id>', views.confirmar_pagamento , name = 'confirm'),
    path('list_all', views.list_all, name = 'list_all'),
]
