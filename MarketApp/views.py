from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods


def index(request):
    return HttpResponse('就当交房租了')


def market(request):
    # 左栏
    foodtypes=AxfFoodType.objects.all()
    # 右上 分类显示
    typeid=request.GET.get('typeid','104749')
    childtypenames=AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    # 全部分类:0#进口水果:103534#国产水果:103533
    childtypenames_list=childtypenames.split('#')
     # ['全部分类:0', '进口水果:103534', '国产水果:103533']
    c_list=[]
    for childtypename in childtypenames_list:

        c= childtypename.split(':')
        c_list.append(c)
        print(c_list)
    # 商品数据展示
    goods_list=AxfGoods.objects.filter(categoryid=typeid)
    childcid=request.GET.get('childcid',0)
    if childcid==0:
        goods_list=goods_list
    else:
        goods_list=goods_list.filter(childcid=childcid)
    # 排序分类展示
    all_sort_list=[
        ['综合排序','0'],
        ['价格升序','1'],
        ['价格降序','2'],
        ['销量升序','3'],
        ['销量降序','4'],
    ]
    all_sort=request.GET.get('all_sort')
    if all_sort=='0':
        pass
    elif all_sort=='1':
        goods_list=goods_list.order_by('price')
    elif all_sort=='2':
        goods_list=goods_list.order_by('-price')
    elif all_sort=='3':
        goods_list=goods_list.order_by('productnum')
    elif all_sort=='4':
        goods_list=goods_list.order_by('-productnum')



    context={
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'c_list':c_list,
        'childcid':childcid,
        'all_sort_list':all_sort_list,
    }

    return render(request,'axf/main/market/market.html',context=context)