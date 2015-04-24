# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_auto_20150422_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
