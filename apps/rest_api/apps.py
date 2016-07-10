from __future__ import unicode_literals

import logging

from django import apps
from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from .classes import APIEndPoint

logger = logging.getLogger('django.request')


class AbstractAppConfig(apps.AppConfig):
    app_url = None
    app_namespace = None

    def ready(self):
        from tracks.urls import urlpatterns

        if self.app_url:
            top_url = '{}/'.format(self.app_url)
        elif self.app_url is not None:
            top_url = ''
        else:
            top_url = '{}/'.format(self.name)

        try:
            urlpatterns += url(
                r'^{}'.format(top_url),
                include(
                    '{}.urls'.format(self.name),
                    namespace=self.app_namespace or self.name
                )
            ),
        except ImportError:
            logger.debug('App %s doesn\'t have URLs defined.', self.name)


class RESTAPIApp(AbstractAppConfig):
    """
    This class registers the app
    """

    app_url = 'api'
    name = 'rest_api'
    verbose_name = _('REST API')

    def ready(self):
        super(RESTAPIApp, self).ready()

        APIEndPoint(app=self, name='rest', version_string='1')
