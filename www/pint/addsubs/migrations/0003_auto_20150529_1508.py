# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addsubs', '0002_auto_20150528_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='delay',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='finished',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='play',
            field=models.BooleanField(),
        ),
    ]
