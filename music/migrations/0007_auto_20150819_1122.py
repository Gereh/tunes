# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_album_publishername'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistCoverImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('img', models.ImageField(upload_to='media/artist/coverImg', default='media/artist/coverImg/default.jpg')),
            ],
        ),
        migrations.RemoveField(
            model_name='artist',
            name='coverImg',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='description',
        ),
        migrations.AddField(
            model_name='artist',
            name='tags',
            field=models.CharField(max_length=25, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artistcoverimage',
            name='artistID',
            field=models.ForeignKey(to='music.Artist'),
        ),
    ]
