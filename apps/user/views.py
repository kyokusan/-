import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user import set_password
from user.forms import UserformModel, User_formModel, InforFormModel, ForgetPassword
from user.models import User

#——————登录  与  注册  与  忘记密码——————————————————————————————————————————
def login(request):#登录
    if request.method=="GET":
        return render(request,"login.html")
    else:
        data=request.POST
        form=User_formModel(data)#验证合法性
        if form.is_valid():
            user=form.cleaned_data.get("user")#获得之前定义在清洗数据里的user信息
            request.session["id"]=user.pk#将SESSION的ID设定为user的ID
            request.session["tel"]=user.tel#将SESSION的TEL设定为user的TEL
            return redirect(reverse("user:member"))
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
            return redirect(reverse("user:login"))
        else:
            context={"errors":form.errors}
            return render(request,"reg.html",context=context)
def forgetpassword(request):#-------------------------------忘记密码页面
    if request.method=="GET":#如果说是GET请求
        return render(request,"forgetpassword.html")
    if request.method=="POST":#如果是POST请求
        data = request.POST#获得表单提交的数据
        form=ForgetPassword(data)#进入表单验证
        if form.is_valid():#如果正确
            tel=form.cleaned_data.get("tel")#获取手机号码
            pwd=set_password(form.cleaned_data.get("password"))#将更新的密码加密
            User.objects.filter(tel=tel).update(password=pwd)#更新密码
            return redirect(reverse("user:login"))#跳转到登录页面
        else:
            context={"errors":form.errors}#定义错误变量
            return render(request,"forgetpassword.html",context=context)#渲染页面



#——————————————————————————————————————————————————

def member(request):#---------------个人中心页面
    if request.session.get("id") is None:#判断SESSION是否存在
        return redirect(reverse("user:login"))#不存在直接跳转LOGIN页面
    else:#如果存在
        return render(request,"member.html")#渲染个人中心页面
def infor(request):#-------------------------个人信息页面
    if request.session.get("id") is None:#判断SESSION是否存在
        return redirect(reverse("user:login"))#不存在跳转LOGIN页面
    if request.method=="GET":#如果是GET方法
        id=request.session.get("id")#获取SESSION上的ID
        data=User.objects.get(pk=id)#查询ID的数据
        context={"data":data}#定义ID为一个变量
        return render(request,"infor.html",context=context)#渲染页面，更新个人资料
    if request.method=="POST":#如果为POST
        id=request.session.get("id")#获取SESSION的ID
        data=request.POST#获得表单提交的数据
        form=InforFormModel(data)#验证数据的合法性
        if form.is_valid():#如果合法
            cleaned_data=form.cleaned_data#获得清洗后的合法数据
            User.objects.filter(pk=id).update(name=cleaned_data.get("name"),birth=cleaned_data.get("birth"),sex=cleaned_data.get("sex"),school=cleaned_data.get("school"),home=cleaned_data.get("home"),location=cleaned_data.get("location"))#更新数据
            return redirect(reverse("user:infor"))#跳转个人资料页面
        else:#如果不合法
            id = request.session.get("id")#获得SESSION的ID
            datas=User.objects.get(pk=id)#获得ID原本的数据
            context={"errors":form.errors,
                     "data":datas}#将原本信息和错误信息渲染到个人资料页面
            return render(request,"infor.html",context=context)#渲染页面
#——————————————————————————————————————————————————
