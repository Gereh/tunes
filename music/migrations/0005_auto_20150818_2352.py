# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_track_playerimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
    ]
