# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'')),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('user', models.ForeignKey(related_name=b'journeys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
