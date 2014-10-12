# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0010_auto_20141012_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='user',
            field=models.ForeignKey(related_name=b'journeys', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
