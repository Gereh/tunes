# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_album_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='facebook',
            field=models.CharField(max_length=100, default='#'),
        ),
        migrations.AddField(
            model_name='artist',
            name='rss',
            field=models.CharField(max_length=100, default='#'),
        ),
        migrations.AddField(
            model_name='artist',
            name='twitter',
            field=models.CharField(max_length=100, default='#'),
        ),
        migrations.AddField(
            model_name='artist',
            name='weblog',
            field=models.CharField(max_length=100, default='#'),
        ),
        migrations.AddField(
            model_name='artist',
            name='website',
            field=models.CharField(max_length=100, default='#'),
        ),
        migrations.AddField(
            model_name='artist',
            name='youtube',
            field=models.CharField(max_length=100, default='#'),
        ),
    ]
