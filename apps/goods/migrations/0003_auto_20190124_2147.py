# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-24 21:47
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_activity_activityzone_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='goods_spu',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='商品SPU详情'),
        ),
    ]
