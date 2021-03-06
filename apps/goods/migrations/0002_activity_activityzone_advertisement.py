# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-23 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='活动名称')),
                ('img_url', models.ImageField(upload_to='activity/%Y%m/%d', verbose_name='活动图片地址')),
                ('url_site', models.URLField(verbose_name='活动的URL地址')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '首页活动',
                'verbose_name_plural': '首页活动',
            },
        ),
        migrations.CreateModel(
            name='ActivityZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='活动专区名字')),
                ('brief', models.CharField(max_length=200, null=True, verbose_name='活动专区的简介')),
                ('order', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('on_sale', models.BooleanField(choices=[(False, '下架'), (True, '上架')], default=0, verbose_name='是否上线')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
                ('goods_sku', models.ManyToManyField(to='goods.Goods_Sku', verbose_name='商品')),
            ],
            options={
                'verbose_name': '活动专区管理',
                'verbose_name_plural': '活动专区管理',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='轮播活动名')),
                ('img_url', models.ImageField(upload_to='advertisement/%Y%m/%d', verbose_name='轮播图片地址')),
                ('order', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
                ('goods_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods_Sku', verbose_name='商品SKU')),
            ],
            options={
                'verbose_name': '轮播管理',
                'verbose_name_plural': '轮播管理',
            },
        ),
    ]
