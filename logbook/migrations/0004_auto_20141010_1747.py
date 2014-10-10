# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0003_auto_20141010_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=10),
            preserve_default=True,
        ),
    ]
