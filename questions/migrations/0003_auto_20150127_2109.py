# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dt',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
