# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='blocking',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='chat_room_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='own_room',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='requested_friends',
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=None, null=True, upload_to=b'photos/', blank=True),
        ),
    ]
