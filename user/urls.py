from django.conf.urls import url

from user.views import login, reg, infor

urlpatterns = [
    url(r'^login/',login,name="login"),
    url(r'^reg/',reg,name="reg"),
    url(r'^infor/',infor,name="infor"),

]