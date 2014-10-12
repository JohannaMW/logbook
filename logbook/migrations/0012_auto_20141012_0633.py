# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0011_auto_20141012_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='main_image',
            field=models.ImageField(upload_to=b'photos'),
        ),
    ]
