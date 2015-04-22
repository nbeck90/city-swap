# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20150422_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='courier',
            field=models.ManyToManyField(related_name='requests', null=True, to='profiles.Profile', blank=True),
        ),
    ]
