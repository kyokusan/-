from django.conf.urls import url

from order.views import allorder, tureorder, order

urlpatterns = [
    url(r'^allorder/',allorder,name="订单"),
url(r'^tureorder/',tureorder,name="确认订单"),
url(r'^order/',order,name="支付页面"),


]