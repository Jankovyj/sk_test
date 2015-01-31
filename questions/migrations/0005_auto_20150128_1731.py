# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 17, 31, 8, 206673, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(to='questions.Question', related_name='comment'),
            preserve_default=True,
        ),
    ]
