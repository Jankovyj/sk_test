# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dt',
            field=models.DateField(default=datetime.datetime(2015, 1, 27, 20, 39, 4, 556322, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
