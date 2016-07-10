from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import url

from .api_views import (
    tags_search_list
)

api_urls = [
    url(r'^playlists/$', tags_search_list, name='tags-search-list'),
]

