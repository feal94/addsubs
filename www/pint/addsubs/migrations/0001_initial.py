# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('video', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('delay', models.IntegerField()),
                ('play', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('hash', models.CharField(max_length=200)),
            ],
        ),
    ]
