# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-03 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_useraddress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
    ]
