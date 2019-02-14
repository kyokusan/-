from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from goods.models import Goods_Sku
from shopCart.helpler import json_msg, get_cart_count, get_cart_key
from django_redis import get_redis_connection

def shopcart(request):
    """购物车展示"""
    if request.method == "GET":
        """
        步骤
        1.从redis获取所以的购物车信息
        2.根据购物车的sku_id从商品 sku表中获取商品信息
        3.渲染的数据
            将购物车的数量和商品信息合成一块儿
        """
        #1。接收参数
        user_id = request.session.get("id")
        #2.操作数据库
        r = get_redis_connection()
        #准备键
        cart_key = get_cart_key(user_id)
        # 从redis获取所有的购物车信息
        cart_datas = r.hgetall(cart_key)
        #准备一个空列表，保存多个商品
        goods_skus=[]
        #遍历字典
        for sku_id,count in cart_datas.items():
            #将二进制转换成整形
            sku_id = int(sku_id)
            count = int(count)

            #2.根据购物车的sku_id从商品sku表单获取商品信息
            try:
                goods_sku=Goods_Sku.objects.get(pk=sku_id,is_delete=False,on_sale=True)
            except Goods_Sku.DoesNotExist:
                #删除redis中过期的数据
                r.hdel(cart_key,sku_id)
                continue

            #3.将购物车的数量和商品信息保存到一块儿(给已经存在的对象添加一个属性)
            setattr(goods_sku,"count",count)

            #保存商品到商品列表
            goods_skus.append(goods_sku)

        #渲染页面
        context={"goods_skus":goods_skus}

        return render(request,"shopcart.html",context=context)

def add(request):
    if request.method == "POST":
        if request.session.get("id") is None:
            if request.is_ajax():
                return JsonResponse(json_msg(1,"未登录老铁，AJAX提示"))
            else:
                return redirect(reverse("user:login"))
        else:

            #接受参数
            user_id = request.session.get("id")
            sku_id=request.POST.get("sku_id")
            count=request.POST.get("count")
            #判断为整数
            try:
                sku_id=int(sku_id)
                count=int(count)
            except:
                return JsonResponse(json_msg(1,"参数错误"))
            #要在数据库中存在的商品
            try:
                goods_sku=Goods_Sku.objects.get(pk=sku_id)
            except Goods_Sku.DoesNotExist:
                return JsonResponse(json_msg(2,"商品不存在"))
            #判断库存
            if goods_sku.stock < count:
                return JsonResponse(json_msg(3,"库存不足"))
            #创建数据
            r = get_redis_connection()
            #处理购物车的 KEY
            cart_key=f"cart_{user_id}"
            #添加
            #获取购物车中已经存在的数量 加上 需要添加 与库存进行比较
            old_count=r.hget(cart_key,sku_id) #二进制
            if old_count is None:
                old_count = 0
            else:
                old_count=int(old_count)
            if goods_sku.stock < old_count + count:
                return  JsonResponse(json_msg(3,"库存不足"))
            #将商品添加到购物车
            rs_count=r.hincrby(cart_key,sku_id,count)
            if rs_count <= 0:
                # 删除filed
                r.hdel(cart_key,sku_id)

            #获取购物车总数量
            cart_count = get_cart_count(request)

            return JsonResponse(json_msg(0,"添加购物车成功",data=cart_count))

def reduce(request):
    if request.method == "POST":
        if request.session.get("id") is None:
            if request.is_ajax():
                return JsonResponse(json_msg(1,"未登录老铁，AJAX提示"))
            else:
                return redirect(reverse("user:login"))
        else:

            #接受参数
            user_id = request.session.get("id")
            sku_id=request.POST.get("sku_id")
            count=request.POST.get("count")
            #判断为整数
            try:
                sku_id=int(sku_id)
                count=int(count)
            except:
                return JsonResponse(json_msg(1,"参数错误"))
            #要在数据库中存在的商品
            try:
                goods_sku=Goods_Sku.objects.get(pk=sku_id)
            except Goods_Sku.DoesNotExist:
                return JsonResponse(json_msg(2,"商品不存在"))
            #判断库存
            if goods_sku.stock < count:
                return JsonResponse(json_msg(3,"库存不足"))
            #创建数据
            r = get_redis_connection()
            #处理购物车的 KEY
            cart_key= get_cart_key(user_id)
            #添加
            #获取购物车中已经存在的数量 加上 需要添加 与库存进行比较
            old_count=r.hget(cart_key,sku_id) #二进制
            if old_count is None:
                old_count = 0
            else:
                old_count=int(old_count)
            if goods_sku.stock < old_count + count:
                return  JsonResponse(json_msg(3,"库存不足"))
            #将商品添加到购物车
            r.hincrby(cart_key,sku_id,count)
            #获取购物车总数量
            cart_count = get_cart_count(request)

            return JsonResponse(json_msg(0,"减少购物车成功",data=cart_count))





