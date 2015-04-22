# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocking',
            field=models.ManyToManyField(related_name='blocked_by', null=True, to='profiles.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='chat_room_name',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='own_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=b'photos/link.jpg', null=True, upload_to=b'photos/', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='requested_friends',
            field=models.ManyToManyField(related_name='requesting_friend', null=True, to='profiles.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.CharField(unique=True, max_length=32, blank=True),
        ),
    ]
