from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from AxfHomeApp.models import AxfWheel, AxfNav, AxfMustBuy, AxfMainShow


def index(request):
    return HttpResponse('天天就给老子装傻')


def home(request):
    wheels=AxfWheel.objects.all()
    navs=AxfNav.objects.all()
    mustbuys=AxfMustBuy.objects.all()
    mainshows=AxfMainShow.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())