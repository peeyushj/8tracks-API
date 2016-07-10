from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import APIBase

urlpatterns = patterns(
    '',
)

api_urls = patterns(
    '',
    url(r'^$', APIBase.as_view(), name='api_root'),
)
