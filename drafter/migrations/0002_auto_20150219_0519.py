# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drafter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='draft_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 5, 19, 37, 651457)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=32, verbose_name=b'Player Name'),
            preserve_default=True,
        ),
    ]
