# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160314_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=100, null=True, blank=True)),
                ('latitude', models.CharField(max_length=100, null=True, blank=True)),
                ('longitude', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('county', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.ForeignKey(to='main.State', null=True)),
            ],
        ),
    ]
