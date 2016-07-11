# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('playlists', '0001_initial'), ('playlists', '0002_remove_playlist_tags'), ('playlists', '0003_auto_20160710_1151'), ('playlists', '0004_auto_20160710_1151'), ('playlists', '0005_playlist_created_on'), ('playlists', '0006_auto_20160710_1709'), ('playlists', '0007_auto_20160710_1712'), ('playlists', '0008_auto_20160710_1712'), ('playlists', '0009_auto_20160710_1714'), ('playlists', '0010_auto_20160710_1721'), ('playlists', '0011_auto_20160710_1751'), ('playlists', '0012_auto_20160710_1803')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('playlist_id', models.AutoField(serialize=False, primary_key=True)),
                ('playlist_name', models.CharField(help_text='Name of the Playlist', max_length=255, verbose_name='playlist_name')),
                ('likes', models.IntegerField(default=0)),
                ('plays', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Added', null=True)),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(serialize=False, primary_key=True)),
                ('tag_name', models.CharField(help_text='Name of the tag', max_length=255, verbose_name='tag_name')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='tags',
            field=models.ManyToManyField(related_name='playlists_with_tags', to=b'playlists.Tag'),
        ),
    ]
