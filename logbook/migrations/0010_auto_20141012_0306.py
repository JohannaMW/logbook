# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0009_remove_journey_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='from_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='to_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
