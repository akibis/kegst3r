# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerData',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('brewery_name', models.CharField(max_length=40)),
                ('beer_type', models.CharField(max_length=40)),
                ('number_dispensed', models.IntegerField(default=0)),
                ('popularity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('badge_number', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=20)),
                ('balance', models.IntegerField(default=0)),
                ('beer_count', models.IntegerField(default=0)),
            ],
        ),
    ]
