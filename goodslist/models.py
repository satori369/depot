from django.db import models

# Create your models here.
#商品类别
class Goods_sort(models.Model):

    name = models.CharField(verbose_name='类别名称',max_length=50)
    introduce = models.CharField(verbose_name='类别介绍',max_length=500)
    is_active = models.BooleanField(verbose_name='删除',default=True)

    class Meta:

        db_table = 'goods_sort'

#商品信息
class Goods_info(models.Model):

    goods_sort = models.ForeignKey(Goods_sort)
    name = models.CharField(max_length=50,verbose_name='商品信息')
    area = models.CharField(verbose_name='产地',max_length=50)
    unit = models.CharField(verbose_name='单位',max_length=50)
    spec = models.CharField(verbose_name='规格',max_length=50)
    remark = models.CharField(verbose_name='备注',max_length=50)
    is_active = models.BooleanField(verbose_name='删除')
    number = models.IntegerField(verbose_name='数量',default=1)

    class Meta:

        db_table = 'goods_info'