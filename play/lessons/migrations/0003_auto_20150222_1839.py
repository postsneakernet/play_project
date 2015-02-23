# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import lessons.models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20150222_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='brief',
            field=models.TextField(default=datetime.datetime(2015, 2, 22, 23, 39, 34, 169126, tzinfo=utc), max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='icon',
            field=models.ImageField(default=datetime.datetime(2015, 2, 22, 23, 39, 44, 49582, tzinfo=utc), upload_to=lessons.models.file_dir),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2015, 2, 22, 23, 39, 57, 898450, tzinfo=utc), upload_to=lessons.models.file_dir),
            preserve_default=False,
        ),
    ]
