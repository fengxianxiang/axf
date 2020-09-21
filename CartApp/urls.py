from django.urls import path

from CartApp import views
app_name='axfcart'
urlpatterns=[
    path('cart/',views.cart,name='cart'),
]