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
