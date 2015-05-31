# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('addsubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='delay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='job',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='play',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
