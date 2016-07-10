# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('playlist_id', models.AutoField(serialize=False, primary_key=True)),
                ('playlist_name', models.CharField(help_text='Name of the Playlist', max_length=255, verbose_name='playlist_name')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('likes', models.IntegerField(default=0)),
                ('plays', models.IntegerField(default=0)),
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
            field=models.ManyToManyField(related_name='playlists_with_tags', verbose_name='tags', to='playlists.Tag'),
        ),
    ]
