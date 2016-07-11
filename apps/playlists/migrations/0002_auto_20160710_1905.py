# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0001_squashed_0012_auto_20160710_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='tags',
            field=models.ManyToManyField(related_name='playlists_with_tags', verbose_name='tags', to='playlists.Tag'),
        ),
    ]
