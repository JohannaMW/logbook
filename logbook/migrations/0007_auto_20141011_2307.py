# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0006_auto_20141010_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='image',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
        ),
    ]
