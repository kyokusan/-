from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class User(models.Model):
    choice=((1,"男"),(2,"女"))
    tel=models.CharField(max_length=11,validators=[MinLengthValidator(7)])
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=32,validators=[MinLengthValidator(6)])
    sex=models.SmallIntegerField(choices=choice,default=1)
    school=models.CharField(max_length=50)
    home=models.CharField(max_length=50)
    is_delete=models.BooleanField(default=False)
    create_time=models.DateField(auto_now_add=True)
    update_time=models.DateField(auto_now=True)
    class Meta:
        db_table="User"
