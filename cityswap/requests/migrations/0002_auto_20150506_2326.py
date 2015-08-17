# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='courier',
        ),
        migrations.AddField(
            model_name='request',
            name='courier',
            field=models.ForeignKey(related_name='requests', blank=True, to='profiles.Profile', null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='destination',
            field=models.CharField(default=b'Seattle', max_length=2, choices=[(b'Seattle', b'Seattle'), (b'Portland', b'Portland')]),
        ),
        migrations.AlterField(
            model_name='request',
            name='origin',
            field=models.CharField(default=b'Seattle', max_length=2, choices=[(b'Seattle', b'Seattle'), (b'Portland', b'Portland')]),
        ),
    ]
