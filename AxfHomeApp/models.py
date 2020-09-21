from django.db import models

# Create your models here.


# 轮播
class AxfWheel(models.Model):
    name=models.CharField(max_length=128)
    img=models.CharField(max_length=64)
    trackid=models.IntegerField(default=1)
    class Meta:
        db_table='axf_wheel'


# 首页-导航
class AxfNav(models.Model):
    name=models.CharField(max_length=128)
    img=models.CharField(max_length=64)
    trackid=models.IntegerField(default=1)
    class Meta:
        db_table='axf_nav'


# 首页-必购
class AxfMustBuy(models.Model):
    name=models.CharField(max_length=128)
    img=models.CharField(max_length=64)
    trackid=models.IntegerField(default=1)
    class Meta:
        db_table='axf_mustbuy'


# 首页-mainshow
class AxfMainShow(models.Model):
    name=models.CharField(max_length=128)
    img=models.CharField(max_length=64)
    trackid=models.IntegerField(default=1)
    categoryid=models.IntegerField(default=1)
    brandname=models.CharField(max_length=64)

    img1=models.CharField(max_length=64)
    childcid1=models.IntegerField(default=1)
    productid1=models.IntegerField(default=1)
    longname1=models.CharField(max_length=128)
    price1=models.FloatField(default=1)
    marketprice1=models.FloatField(default=1)

    img2=models.CharField(max_length=64)
    childcid2=models.IntegerField(default=1)
    productid2=models.IntegerField(default=1)
    longname2=models.CharField(max_length=128)
    price2=models.FloatField(default=1)
    marketprice2=models.FloatField(default=1)

    img3=models.CharField(max_length=64)
    childcid3=models.IntegerField(default=1)
    productid3=models.IntegerField(default=1)
    longname3=models.CharField(max_length=128)
    price3=models.FloatField(default=1)
    marketprice3=models.FloatField(default=1)

    class Meta:
        db_table='axf_mainshow'