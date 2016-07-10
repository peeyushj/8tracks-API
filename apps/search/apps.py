from __future__ import absolute_import, unicode_literals

from django import apps
from django.utils.translation import ugettext_lazy as _

from rest_api.classes import APIEndPoint


class SearchApp(apps.AppConfig):
    name = 'search'
    test = True
    verbose_name = _('Search')

    def ready(self):
        super(SearchApp, self).ready()

        APIEndPoint(app=self, version_string='1')
