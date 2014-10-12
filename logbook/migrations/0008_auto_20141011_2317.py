# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0007_auto_20141011_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journey',
            old_name='image',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='journey',
            name='image_2',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='image_3',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='image_4',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='image_5',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journey',
            name='main_image',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
    ]
