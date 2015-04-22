# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150422_1854'),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='currier',
        ),
        migrations.AddField(
            model_name='request',
            name='courier',
            field=models.ManyToManyField(default=None, related_name='requests', to='profiles.Profile'),
        ),
    ]
