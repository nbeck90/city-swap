# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150422_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'Type your info here')),
                ('origin', models.CharField(default=b'se', max_length=2, choices=[(b'se', b'Seattle'), (b'pt', b'Portland')])),
                ('destination', models.CharField(default=b'se', max_length=2, choices=[(b'se', b'Seattle'), (b'pt', b'Portland')])),
                ('currier', models.ManyToManyField(related_name='requests', to='profiles.Profile')),
                ('sender', models.ForeignKey(related_name='sent_from', to='profiles.Profile')),
            ],
        ),
    ]
