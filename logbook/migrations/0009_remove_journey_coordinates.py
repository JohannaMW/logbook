# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0008_auto_20141011_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='coordinates',
        ),
    ]
