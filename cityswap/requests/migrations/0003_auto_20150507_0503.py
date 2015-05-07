# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20150506_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='destination',
            field=models.CharField(default=b'Seattle', max_length=25, choices=[(b'Seattle', b'Seattle'), (b'Portland', b'Portland')]),
        ),
        migrations.AlterField(
            model_name='request',
            name='origin',
            field=models.CharField(default=b'Seattle', max_length=25, choices=[(b'Seattle', b'Seattle'), (b'Portland', b'Portland')]),
        ),
    ]
