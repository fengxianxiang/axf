from django.urls import path

from MineApp import views
app_name='axfmine'

urlpatterns=[
    path('mine/',views.mine,name='mine'),
]