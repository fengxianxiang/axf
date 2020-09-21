from django.urls import path

from AxfHomeApp import views
app_name='axfname'

urlpatterns=[
    path('index/',views.index),
    path('home/',views.home,name='home'),


]