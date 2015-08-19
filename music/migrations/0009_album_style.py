# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20150819_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='style',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]
