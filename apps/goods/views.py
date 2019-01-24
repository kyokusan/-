from django.shortcuts import render

# Create your views here.
from django.views import View

from goods.models import Goods_Sku, Goods_Spu


def index(request):#商城主页
    if request.method=="GET":
        data=Goods_Sku.objects.filter(is_delete=False)
        context={"data":data}
        return render(request,"index.html",context=context)

def detail(request,id):
    # Spu=Goods_Spu.objects.get(pk=id)
    Sku=Goods_Sku.objects.get(pk=id)
    context={"Sku":Sku}
    return render(request,"detail.html",context=context)

def category(request):#商品类别
    if request.method=="GET":
        return render(request,"category.html")

