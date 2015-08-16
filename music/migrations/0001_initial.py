# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import music.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('userName', models.CharField(max_length=50, unique=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('balance', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('licenseNo', models.CharField(max_length=50)),
                ('publishDate', models.DateTimeField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('adminID', models.ForeignKey(to='music.Admin')),
                ('albumID', models.ForeignKey(to='music.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('bio', models.TextField()),
                ('profileImg', models.ImageField(default='media/artist/profileImg/default.jpg', upload_to='media/artist/profileImg')),
                ('coverImg', models.ImageField(default='media/artist/coverImg/default.jpg', upload_to='media/artist/coverImg')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('bank', models.CharField(max_length=20)),
                ('receiptNo', models.CharField(max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('isConfirmed', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('albumID', models.ForeignKey(to='music.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('likeCount', models.IntegerField(default=0)),
                ('isPublic', models.BooleanField(default=True)),
                ('isGeneral', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('artistID', models.ForeignKey(to='music.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='SiteTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.FileField(upload_to='')),
                ('rateCount', models.IntegerField()),
                ('rate', models.IntegerField(default=0, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('lyric', models.TextField(blank=True)),
                ('poet', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('albumID', models.ForeignKey(to='music.Album')),
                ('artistID', models.ManyToManyField(to='music.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('userName', models.CharField(max_length=30, unique=music.models.Track, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, blank=True)),
                ('address', models.TextField(blank=True)),
                ('balance', models.IntegerField(default=0)),
                ('isGold', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('lastLogin', models.DateTimeField(blank=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sitetransaction',
            name='userID',
            field=models.ForeignKey(to='music.User'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='trackID',
            field=models.ForeignKey(to='music.Track'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='userID',
            field=models.ForeignKey(to='music.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postID',
            field=models.ForeignKey(to='music.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userID',
            field=models.ForeignKey(to='music.User'),
        ),
        migrations.AddField(
            model_name='banktransaction',
            name='userID',
            field=models.ForeignKey(to='music.User'),
        ),
        migrations.AddField(
            model_name='album',
            name='artistID',
            field=models.ManyToManyField(to='music.Artist'),
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together=set([('userID', 'trackID')]),
        ),
    ]
