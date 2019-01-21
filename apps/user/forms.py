

from django import forms
from django.core.validators import RegexValidator

from user import set_password
from user.models import User



class UserformModel(forms.ModelForm):#----------------------------------------定义一个注册的表单验证
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})#单独验证 因为数据库没有repassword 无法在最下面一起验证
    repassword=forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})
    def clean_tel(self):#清洗手机号码数据
        tel=self.cleaned_data.get("tel")
        flag=User.objects.filter(tel=tel).exists()#是否存在
        if flag:
            raise forms.ValidationError("用户名存在")
        else:
            return tel
    def clean(self):#清洗全部数据
        pwd=self.cleaned_data.get("password")
        repwd=self.cleaned_data.get("repassword")
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({"repassword":"两次密码不一样"})
        else:
            return self.cleaned_data
    class Meta:
        model=User#验证表单User
        fields=["tel",]#只能先验证tel


class User_formModel(forms.ModelForm): #--------------------------------定义一个登录表单的验证
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})
    # repassword=forms.CharField(max_length=20, min_length=6,
    #                            error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})

    def clean(self):#清洗数据
        tel=self.cleaned_data.get("tel")#获得提交的手机号码
        try:
            user=User.objects.get(tel=tel)#查询数据库里是否有提交的手机号码
        except User.DoesNotExist:#如果不存在
            raise forms.ValidationError({"tel":"手机号错误了哦"})
        password=self.cleaned_data.get("password","")#获得提交的密码
        if user.password !=set_password(password):#判断提交的密码和数据库的密码是否一致
            raise forms.ValidationError({"password":"密码错了哦"})#不一致提示错误
        self.cleaned_data["user"]=user#将提交的并且存在的手机号码对象设定为清洗后的数据里的变量（包含所有此手机号的信息）
        return self.cleaned_data#返回清洗后的数据
    class Meta:
        model=User
        fields=["tel",]

class InforFormModel(forms.ModelForm):#-------------------------------------------修改个人资料表单验证
    class Meta:
        model=User
        fields=["name","location","birth","home","sex","school"]

class ForgetPassword(forms.ModelForm):# ------------------------------------------忘记密码表单验证
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6",
                                               "max_length": "最大长度为20"})  # 单独验证 因为数据库没有repassword 无法在最下面一起验证
    repassword = forms.CharField(max_length=20, min_length=6,
                                 error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})
    def clean_tel(self):#清洗手机数据
        tel=self.cleaned_data.get("tel")
        flag=User.objects.filter(tel=tel).exists()#如果存在
        if flag:#存在
            return tel
        else:#不存在
            raise forms.ValidationError("手机号码不存在")
    def clean(self):#清洗所有数据
        pwd=self.cleaned_data.get("password")#获得密码
        repwd=self.cleaned_data.get("repassword")#获确认密码
        if pwd and repwd and pwd != repwd:#验证是否不一致
            raise forms.ValidationError({"repassword":"两次密码不一致"})
        else:
            return self.cleaned_data
    class Meta:
        model=User
        fields = ["tel"]#验证TEL的合法性