# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_page', '0002_auto_20151006_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='badge_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
