# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-07 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品信息')),
                ('area', models.CharField(max_length=50, verbose_name='产地')),
                ('unit', models.CharField(max_length=50, verbose_name='单位')),
                ('spec', models.CharField(max_length=50, verbose_name='规格')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
                ('is_active', models.BooleanField(verbose_name='删除')),
            ],
            options={
                'db_table': 'good_info',
            },
        ),
        migrations.CreateModel(
            name='Goods_sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='类别名称')),
                ('introduce', models.CharField(max_length=500, verbose_name='类别介绍')),
                ('is_active', models.BooleanField(verbose_name='删除')),
            ],
            options={
                'db_table': 'good_sort',
            },
        ),
        migrations.AddField(
            model_name='goods_info',
            name='goods_sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodslist.Goods_sort'),
        ),
    ]