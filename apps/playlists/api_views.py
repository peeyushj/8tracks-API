from __future__ import absolute_import, unicode_literals

import logging

from rest_framework import generics

from .models import (
    PlayList,
    Tag,
)
from .serializers import (
    NewPlaylistPostSerializer,
    PlaylistsListSerializer,
    PlaylistDetailSerializer,
    UpdatePlaylistSerializer,
    TagsListSerializer,
    NewTagPostSerializer,
    TagDetailSerializer,
    UpdateTagSerializer
)

logger = logging.getLogger('django.request')


class APIPlaylistListView(generics.ListCreateAPIView):
    """Returns a list of all the playlists"""

    queryset = PlayList.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaylistsListSerializer
        elif self.request.method == 'POST':
            return NewPlaylistPostSerializer

    def get(self, *args, **kwargs):
        """Get the playlist list."""

        return super(APIPlaylistListView, self).get(*args, **kwargs)

playlists_list = APIPlaylistListView.as_view()


class APIPlaylistDetailView(generics.RetrieveUpdateAPIView):
    """Returns the selected playlist details."""

    queryset = PlayList.objects.all()
    lookup_field = 'playlist_id'

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return PlaylistDetailSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdatePlaylistSerializer

    def get(self, *args, **kwargs):
        """Return the details of the selected playlist"""
        return super(APIPlaylistDetailView, self).get(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return super(APIPlaylistDetailView, self).patch(*args, **kwargs)

playlist_detail = APIPlaylistDetailView.as_view()


class APITagListView(generics.ListCreateAPIView):
    """Returns a list of all the Tags."""

    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TagsListSerializer
        elif self.request.method == 'POST':
            return NewTagPostSerializer

    def get(self, *args, **kwargs):
        """Get the Tag list."""

        return super(APITagListView, self).get(*args, **kwargs)

tags_list = APITagListView.as_view()


class APITagDetailView(generics.RetrieveUpdateAPIView):
    """Returns the selected Tag details."""

    queryset = Tag.objects.all()
    lookup_field = 'tag_id'

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TagDetailSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateTagSerializer

    def get(self, *args, **kwargs):
        """Return the details of the selected Tag."""

        return super(APITagDetailView, self).get(*args, **kwargs)

    def patch(self, *args, **kwargs):

        return super(APITagDetailView, self).patch(*args, **kwargs)

tag_detail = APITagDetailView.as_view()
