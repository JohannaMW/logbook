# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0004_auto_20141010_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=10, blank=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=10, blank=True),
        ),
    ]
