# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(default=b'Type your title here')),
                ('description', models.TextField(default=b'Type your description here')),
                ('origin', models.CharField(default=b'se', max_length=2, choices=[(b'se', b'Seattle'), (b'pt', b'Portland')])),
                ('destination', models.CharField(default=b'se', max_length=2, choices=[(b'se', b'Seattle'), (b'pt', b'Portland')])),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('courier', models.ManyToManyField(related_name='requests', null=True, to='profiles.Profile', blank=True)),
                ('sender', models.ForeignKey(related_name='sent_from', to='profiles.Profile')),
            ],
        ),
    ]
