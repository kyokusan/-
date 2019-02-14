# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-03 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='运输方式')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='运费')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '运输方式管理',
                'verbose_name_plural': '运输方式管理',
            },
        ),
    ]