# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100)),
                ('delay', models.IntegerField(null=True)),
                ('play', models.BooleanField()),
                ('finished', models.BooleanField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50, null=True)),
                ('year', models.IntegerField(null=True)),
                ('hash', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='video',
            field=models.ForeignKey(to='addsubs.Movie'),
        ),
    ]
