# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.DeleteModel(
            name='CorrectAnswer',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_correct_answer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
