from django.conf.urls import url

from shopCart.views import add, reduce, shopcart

urlpatterns = [
    url(r'^add/',add,name="添加"),
    url(r'^reduce/', reduce, name="减少"),
    url(r'shopcart/', shopcart, name="购物车"),
    ]