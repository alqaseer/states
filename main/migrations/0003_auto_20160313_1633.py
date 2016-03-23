# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160310_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='capital',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='capital_population',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
