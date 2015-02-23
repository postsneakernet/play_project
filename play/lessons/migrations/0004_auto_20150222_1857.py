# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lessons.models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20150222_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='icon',
            field=models.ImageField(upload_to=lessons.models.lesson_dir),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='photo',
            field=models.ImageField(upload_to=lessons.models.lesson_dir),
            preserve_default=True,
        ),
    ]
