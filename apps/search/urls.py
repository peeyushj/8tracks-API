from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import url

from .api_views import (
    tags_search_list,
    relavent_tags
)

api_urls = [
    url(r'^playlists/$', tags_search_list, name='tags-search-list'),
    url(r'^tags/$', relavent_tags, name='relavent-tags'),
]

