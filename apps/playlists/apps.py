from __future__ import absolute_import, unicode_literals

from django import apps
from django.utils.translation import ugettext_lazy as _

from rest_api.classes import APIEndPoint


class PlaylistsApp(apps.AppConfig):
    """
    This class does the customized registration of the app.
    """

    name = 'playlists'
    test = True
    verbose_name = _('playlists')

    def ready(self):
        super(PlaylistsApp, self).ready()

        APIEndPoint(app=self, version_string='1')
