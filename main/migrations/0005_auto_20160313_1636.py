# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160313_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
