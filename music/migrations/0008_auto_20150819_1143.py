# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20150819_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistPoster',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('img', models.ImageField(default='music/artistposter/img/default.jpg', upload_to='music/artistposter/img')),
            ],
        ),
        migrations.RemoveField(
            model_name='artistcoverimage',
            name='artistID',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='profileImg',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='tags',
        ),
        migrations.AddField(
            model_name='artist',
            name='backImg',
            field=models.ImageField(default='music/artist/backimg/default.jpg', upload_to='music/artist/backimg'),
        ),
        migrations.AddField(
            model_name='artist',
            name='title',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ArtistCoverImage',
        ),
        migrations.AddField(
            model_name='artistposter',
            name='artistID',
            field=models.ForeignKey(to='music.Artist'),
        ),
    ]
