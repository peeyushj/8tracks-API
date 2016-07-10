from __future__ import absolute_import, unicode_literals

import logging

from django.utils.translation import ugettext_lazy as _

from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from playlists.serializers import PlaylistsListSerializer
from search.pagination import SearchListPagination

from playlists.models import Tag
from .utils import (
    Q_PARAM,
)

logger = logging.getLogger('django.request')


class APISearchListViewBase(generics.ListAPIView):
    """
    The base view for handling search results for:
    `tags`

    I have used a custom pagination here called `SearchListPagination`. Check search/pagination.py
    for seeing the functionality performed by `SearchListPagination`.
    """

    filter_backends = ()
    pagination_class = SearchListPagination

    allowed_inputs = (Q_PARAM, )

    default_error_messages = {
        'query_necessary_parameter': _('query parameter `q` needs to be given'),
    }

    def get_serializer_class(self):
        raise NotImplementedError('subclasses of APISearchListViewBase should provide this method')

    def get(self, *args, **kwargs):

        q_param = self.request.query_params.get(Q_PARAM, None)

        if not q_param:
            raise ValidationError(detail={'detail':
                self.default_error_messages['query_necessary_parameter']})

        return super(APISearchListViewBase, self).get(*args, **kwargs)


class APISearchListViewThroughTags(APISearchListViewBase):

    def get_serializer_class(self):
        return PlaylistsListSerializer

    def get_queryset(self):
        search_result_queryset = SearchQuerySet().filter(content=AutoQuery(self.request.GET.get(Q_PARAM))).models(
            Tag)
        return search_result_queryset

tags_search_list = APISearchListViewThroughTags.as_view()
