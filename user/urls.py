from django.conf.urls import url

from user.views import login, reg

urlpatterns = [
    url(r'^login/',login,name="login"),
    url(r'^reg/',reg,name="reg"),
]