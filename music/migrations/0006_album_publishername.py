# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20150818_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='publisherName',
            field=models.CharField(max_length=30, default='test'),
            preserve_default=False,
        ),
    ]
