

from django import forms

from user import set_password
from user.models import User



class UserformModel(forms.ModelForm):#定义一个注册的表单验证
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


class User_formModel(forms.ModelForm):
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})
    # repassword=forms.CharField(max_length=20, min_length=6,
    #                            error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})

    def clean(self):
        tel=self.cleaned_data.get("tel")
        try:
            user=User.objects.get(tel=tel)
        except User.DoesNotExist:
            raise forms.ValidationError({"tel":"手机号错误了哦"})
        password=self.cleaned_data.get("password","")
        if user.password !=set_password(password):
            raise forms.ValidationError({"password":"密码错了哦"})
        return self.cleaned_data
    class Meta:
        model=User
        fields=["tel",]