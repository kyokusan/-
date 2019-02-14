from django.shortcuts import render

# Create your views here.
from django.views import View

from goods.models import Goods_Sku, Goods_Spu, Category, Advertisement
from shopCart.helpler import get_cart_count


def index(request):#商城主页
    if request.method=="GET":
        data=Goods_Sku.objects.filter(is_delete=False)
        adv=Advertisement.objects.filter(is_delete=False)
        context={"data":data,"adv":adv}
        return render(request,"index.html",context=context)

def detail(request,id):
    # Spu=Goods_Spu.objects.get(pk=id)
    Sku=Goods_Sku.objects.get(pk=id)

    context={"Sku":Sku}
    return render(request,"detail.html",context=context)

def category(request,cate_id,order):#商品类别
    if request.method=="GET":
        data=Category.objects.filter(is_delete=False).order_by("order")
        if cate_id=="":
            datas=data.first()#第一个类，如果是cata_id没有传值
            cate_id=datas.pk
        else:#如果有参数
            cate_id=int(cate_id)
            datas=Category.objects.filter(pk=cate_id)
        Sku=Goods_Sku.objects.filter(is_delete=False,category=datas)

        if order =="":
            order=0
        order = int(order)

        order_rule = ['pk','-sales_volume','price','-price','-add_time']
        Sku = Sku.order_by(order_rule[order])


        cart_count = get_cart_count(request)
#

        context={"data":data,"Sku":Sku,"cate_id":cate_id,"order":order,"cart_count":cart_count}
        return render(request,"category.html",context=context)

