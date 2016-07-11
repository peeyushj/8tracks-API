from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# create your models here.
class Tag(models.Model):
    """
    Defines a single tag in
    the system.
    """

    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, help_text=_('Name of the tag'),
                            verbose_name=_('tag_name'))

    def __str__(self):
        return ('tag name is: %s') % self.tag_name


class PlayList(models.Model):
    """
    Defines a single Playlist with properties such as
    likes, plays.
    """

    playlist_id = models.AutoField(primary_key=True)
    playlist_name = models.CharField(max_length=255, help_text=_('Name of the Playlist'),
                                verbose_name=_('playlist_name'))

    created_on = models.DateTimeField(verbose_name=_('Added'), auto_now_add=True, null=True)
    likes = models.IntegerField(default=0)
    plays = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, related_name='playlists_with_tags', verbose_name=_('tags'))

    class Meta:
        verbose_name = _('Playlist')
        verbose_name_plural = _('Playlists')

    def __str__(self):
        return ('Playlist unique id: %s') % self.playlist_id
