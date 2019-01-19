from django import forms

from user.models import User


class UserformModel(forms.ModelForm):
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})
    repassword=forms.CharField(max_length=20, min_length=6,
                               error_messages={"min_length": "最小长度为6", "max_length": "最大长度为20"})
    def clean(self):
        pwd=self.cleaned_data.get("password")
        repwd=self.cleaned_data.get("repassword")
        if pwd and repwd and pwd != repwd:
            raise forms.ValidationError({"repassword":"两次密码不一样"})
        else:
            return self.cleaned_data
    class Meta:
        model=User
        fields=["tel",]