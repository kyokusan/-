from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
or_sale=((False,"下架"),(True,"上架"))
class Category(models.Model):#商品分类表
    cata_name=models.CharField(max_length=20,verbose_name="分类名称")
    brief=models.TextField(max_length=200,verbose_name="简介",null=True)
    order=models.SmallIntegerField(default=0,verbose_name="排序")
    add_time=models.DateField(auto_now_add=True,verbose_name="添加时间")
    update_time=models.DateField(auto_now=True,verbose_name="更新时间")
    is_delete=models.BooleanField(default=True,verbose_name="是否删除")
    def __str__(self):
        return self.cata_name
    class Meta:
        verbose_name="商品类别"
        verbose_name_plural=verbose_name

class Goods_Spu(models.Model):#商品SPU表
    spu_name=models.CharField(max_length=20,verbose_name="商品SPU名称")
    detail=RichTextUploadingField(verbose_name="商品SPU详情",null=True)
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.spu_name
    class Meta:
        verbose_name="商品SPU表"
        verbose_name_plural=verbose_name

class Goods_Sku(models.Model):#商品Sku表
    sku_name=models.CharField(max_length=20,verbose_name="商品sku表名称")
    brif=models.TextField(verbose_name="商品SPU简介",null=True)
    price=models.DecimalField(max_digits=9,verbose_name="价格",decimal_places=2,default=0)
    unit=models.ForeignKey(to="Unit",verbose_name="单位")
    stock=models.IntegerField(default=0,verbose_name="库存")
    sales_volume=models.IntegerField(default=0,verbose_name="销量")
    logo=models.ImageField(upload_to="goods/%Y%m/%d",verbose_name="封面图片")
    on_sale=models.BooleanField(verbose_name="是否上架",choices=or_sale,default=False)
    category=models.ForeignKey(to="Category",verbose_name="商品分类")
    goods_spu=models.ForeignKey(to="Goods_Spu",verbose_name="商品SPU")
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.sku_name
    class Meta:
        verbose_name="商品SKU表"
        verbose_name_plural=verbose_name
class Unit(models.Model):#商品单位表
    unit_name=models.CharField(verbose_name="单位",max_length=20)
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.unit_name
    class Meta:
        verbose_name="商品单位管理"
        verbose_name_plural=verbose_name

class Goodsphoto(models.Model):#商品相册表
    img_url=models.ImageField(verbose_name="相册图片地址",upload_to="goods_photo/%Y%m/%d")
    goods_sku=models.ForeignKey(to="Goods_Sku",verbose_name="商品SKU")
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return "商品相册：{}".format(self.img_url.name)
    class Meta:
        verbose_name="商品相册"
        verbose_name_plural=verbose_name

class Advertisement(models.Model):#首页轮播商品
    name=models.CharField(verbose_name="轮播活动名",max_length=150)
    img_url=models.ImageField(verbose_name="轮播图片地址",upload_to="advertisement/%Y%m/%d")
    order=models.SmallIntegerField(verbose_name="排序",default=0)
    goods_sku=models.ForeignKey(verbose_name="商品SKU",to="Goods_Sku")
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="轮播管理"
        verbose_name_plural=verbose_name

class Activity(models.Model):#首页活动表
    title=models.CharField(verbose_name="活动名称",max_length=150)
    img_url=models.ImageField(verbose_name="活动图片地址",upload_to="activity/%Y%m/%d")
    url_site=models.URLField(verbose_name="活动的URL地址",max_length=200)
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="首页活动"
        verbose_name_plural=verbose_name

class ActivityZone(models.Model):#活动专区
    title=models.CharField(max_length=150,verbose_name="活动专区名字")
    brief=models.CharField(verbose_name="活动专区的简介",max_length=200,null=True)
    order=models.SmallIntegerField(default=0,verbose_name="排序")
    on_sale=models.BooleanField(verbose_name="是否上线",choices=or_sale,default=0)
    goods_sku=models.ManyToManyField(to="Goods_Sku",verbose_name="商品")
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=True, verbose_name="是否删除")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "活动专区管理"
        verbose_name_plural = verbose_name

