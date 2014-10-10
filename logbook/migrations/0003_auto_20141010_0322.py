# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0002_journey_coordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
