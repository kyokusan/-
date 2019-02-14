from django.conf.urls import url

from user.views import login, reg, infor, member, forgetpassword, SendMsm, address, gladdress

urlpatterns = [
    url(r'^login/',login,name="login"),
    url(r'^reg/',reg,name="reg"),
    url(r'^infor/',infor,name="infor"),
    url(r'^member/',member,name="member"),
    url(r'^forgetpassword/',forgetpassword,name="forgetpassword"),
    url(r'^sendMsg/$',SendMsm.as_view(),name="发送信息"),
    url(r'^address/$',address,name="新建收货地址"),
    url(r'^gladdress/$', gladdress, name="管理收货地址"),

]