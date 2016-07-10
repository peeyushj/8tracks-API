from __future__ import absolute_import

from django.conf.urls import url

from .api_views import (
    playlists_list,
    playlist_detail,
    tags_list,
    tag_detail,
)

api_urls = [
    url(r'^playlists/$', playlists_list, name='playlists-list'),
    url(
        r'^playlists/(?P<playlist_id>[\w-]+)/$', playlist_detail,
        name='playlists-detail'
    ),
    url(r'^tags/$', tags_list, name='tag-list'),
    url(r'^tags/(?P<tag_id>[\w-]+)/$', tag_detail, name='tag-detail'),
]
