# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drafter', '0002_auto_20150219_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fantasyteam',
            name='name',
            field=models.CharField(default=b'The Bedazzling Defaults', max_length=32, verbose_name=b'Fantasy Team Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='draft_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 5, 21, 23, 59038)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='league',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'League name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'Team Name'),
            preserve_default=True,
        ),
    ]
