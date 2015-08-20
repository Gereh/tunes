# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20150820_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lastLogin',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
