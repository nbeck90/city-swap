# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=b'photos/frame.jpg', null=True, upload_to=b'photos/', blank=True)),
                ('slug', models.CharField(unique=True, max_length=32, blank=True)),
                ('blocking', models.ManyToManyField(related_name='blocked_by', null=True, to='profiles.Profile', blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', null=True, to='profiles.Profile', blank=True)),
                ('requested_friends', models.ManyToManyField(related_name='requesting_friend', null=True, to='profiles.Profile', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
