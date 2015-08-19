# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20150819_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='website',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
