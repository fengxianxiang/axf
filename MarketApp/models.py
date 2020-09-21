from django.db import models

# Create your models here.

class AxfFoodType(models.Model):
    typeid=models.CharField(max_length=32)
    typename=models.CharField(max_length=64)
    childtypenames=models.CharField(max_length=128)
    typesort=models.IntegerField(default=1)
    class Meta:
        db_table='axf_foodtype'


# INSERT INTO axf_goods
# (id, productid, productimg, productname, productlongname, isxf, pmdesc,
# specifics, price, marketprice, categoryid, childcid, childcidname, dealerid, storenums, productnum)
# VALUES (1, 11951, '/media/images/goods016.jpg', '',
# '乐吧薯片鲜虾味50.0g', 0, 0, '50g', 2, 2.5, 103541, 103543,
# '膨化食品', 4858, 200, 4);

class AxfGoods(models.Model):
    productid = models.IntegerField(default=1)
    productimg = models.CharField(max_length=64)
    productname = models.CharField(max_length=32)
    productlongname = models.CharField(max_length=64)
    isxf = models.BooleanField(default=False)
    # 排序规则
    pmdesc = models.IntegerField(default=1)
    # 商品详情
    specifics = models.CharField(max_length=32)
    price = models.FloatField(default=1)
    marketprice =models.FloatField(default=1)
    # 类别的id
    categoryid = models.IntegerField(default=1)
    # 子类别的id 二级联动 三级联动
    childcid = models.IntegerField(default=1)

    childcidname = models.CharField(max_length=64)
    # 商家id
    dealerid = models.IntegerField(default=1)
    # 商店的储备数量
    storenums = models.IntegerField(default=200)
    # 商品的数据
    productnum = models.IntegerField(default=2)

    class Meta:
        db_table='axf_goods'