# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-16 13:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='\u8bc4\u8bba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8bc4\u8bba',
                'verbose_name_plural': '\u8bfe\u7a0b\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a')),
                ('course_name', models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u54a8\u8be2',
                'verbose_name_plural': '\u7528\u6237\u54a8\u8be2',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5b66\u4e60\u8fc7\u7684\u8bfe\u7a0b',
                'verbose_name_plural': '\u7528\u6237\u5b66\u4e60\u8fc7\u7684\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570\u636e Id')),
                ('fav_type', models.IntegerField(choices=[(1, b'\xe8\xaf\xbe\xe7\xa8\x8b'), (2, b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x9c\xba\xe6\x9e\x84'), (3, b'\xe8\xae\xb2\xe5\xb8\x88')], default=1, verbose_name='\u6536\u85cf\u7c7b\u578b')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='\u63a5\u53d7\u7528\u6237')),
                ('message', models.CharField(max_length=500, verbose_name='\u6d88\u606f\u5185\u5bb9')),
                ('has_read', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8bfb')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6d88\u606f',
                'verbose_name_plural': '\u7528\u6237\u6d88\u606f',
            },
        ),
    ]
