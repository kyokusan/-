import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user import set_password
from user.forms import UserformModel, User_formModel
from user.models import User

#___登录与注册__________________________________________________________________________
def login(request):#登录
    if request.method=="GET":
        return render(request,"login.html")
    else:
        data=request.POST
        form=User_formModel(data)#验证合法性
        if form.is_valid():
            return render(request,"infor.html")
        else:
            context={"errors":form.errors}
            return render(request,"login.html",context=context)
def reg(request):#注册页面
    if request.method=="GET":
        return render(request,"reg.html")
    else:
        data=request.POST#得到提交的数据
        form=UserformModel(data)#验证合法性
        if form.is_valid():
            cleaned_data=form.cleaned_data#清洗数据
            user=User()#连接数据库User
            user.tel=cleaned_data.get("tel")#获得清洗后的数据
            user.password=set_password(cleaned_data.get("password"))
            user.save()
            return redirect(reverse("user:infor"))
        else:
            context={"errors":form.errors}
            return render(request,"reg.html",context=context)

#______________________________________________________________________________________

def infor(request):
    if request.method=="GET":
        return render(request,"infor.html")