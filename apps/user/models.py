from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

# Create your models here.
class User(models.Model):#定义表单
    choice=((1,"男"),(2,"女"))
    tel=models.CharField(max_length=11,validators=[RegexValidator(r'1[35678]\d{9}')])
    name=models.CharField(max_length=20,null=True)
    birth=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=32,validators=[MinLengthValidator(6)])
    sex=models.SmallIntegerField(choices=choice,default=1)
    school=models.CharField(max_length=50,null=True)
    home=models.CharField(max_length=50,null=True)
    is_delete=models.BooleanField(default=False)
    create_time=models.DateField(auto_now_add=True)
    update_time=models.DateField(auto_now=True)
    location=models.CharField(max_length=50,null=True)
    head = models.ImageField(upload_to='shop/%Y%m/%d', default='head/memtx.png', verbose_name='用户头像')
    class Meta:#更名
        db_table="User"
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


class UserAddress(models.Model):
    """用户收货地址管理"""
    user = models.ForeignKey(to="User", verbose_name="创建人")
    username = models.CharField(verbose_name="收货人", max_length=100)
    phone = models.CharField(verbose_name="收货人电话", max_length=11,
                             validators=[
                                 RegexValidator("^1[3-9]\d{9}$","电话格式错误")
                             ])
    hcity = models.CharField(verbose_name="省", max_length=100)
    hproper = models.CharField(verbose_name="省", max_length=100, blank=True, null=True)
    harea = models.CharField(verbose_name="省", max_length=100, blank=True, null=True)
    brief = models.CharField(verbose_name="详细地址", max_length=255)
    isDefault = models.BooleanField(verbose_name="是否设置为默认", default=False)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "收货地址管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{}:{}".format(self.username,self.phone)

