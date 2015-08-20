# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_album_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileImg',
            field=models.ImageField(default='user/profileimg/default.jpg', upload_to='user/profileimg'),
        ),
    ]
