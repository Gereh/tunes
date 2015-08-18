# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20150818_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(null=True, max_length=50, blank=True)),
                ('link', models.CharField(default='#', max_length=100)),
                ('position', models.CharField(default='home', max_length=20)),
                ('img', models.ImageField(default='music/advertise/img/default.jpg', upload_to='music/advertise/img')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
