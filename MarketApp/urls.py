from django.urls import path

from MarketApp import views
app_name='axfmarket'

urlpatterns=[
    path('index/',views.index),
    path('market/',views.market,name='market'),
]