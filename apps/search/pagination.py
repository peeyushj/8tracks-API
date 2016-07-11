"""
The module describes a custom Pagination Class and Custom Paginator. This is because the queryset
that we get is a `SearchQuerySet` and not a default `Django QuerySet`. Since the REST API requires model
objects to be finally represented in the HttpResponse, we need to convert each `SearchResult` in `SearchQuerySet`
to model objects
"""

from django.conf import settings
from django.core.paginator import Page
from django.core.paginator import Paginator

from rest_framework.pagination import PageNumberPagination

from playlists.services import get_playlists, sort_playlists_by_likes, sort_playlists_by_plays


class SearchPaginator(Paginator):

    def _get_page(self, *args, **kwargs):
        """
        It returns an instance of a single page. This hook is to be used by subclasses to use an
        alternative to the standard :cls:`Page` object. 
        Searching is done with the help of primary keys of playlists.

        """

        entity_pks = []
        entity_list = []
        qst = []

        for each in args[0]:
            entity_pks.append(each.pk)

        if len(entity_pks) > 0:
            # Get the model involved in the search
            model = args[0][0].model

            # order playlist id in the desc order:
            ordering = 'FIELD(`playlist_id`, %s)' % ','.join(str(id) for id in entity_pks)

            # Get the required playlist elements
            entity_list = model.objects.filter(pk__in=entity_pks).extra(
                select={'ordering': ordering}, order_by=('ordering',))

            # Get the required models of playlists
            playlist_pk_list = []
            for each in entity_list:
                playlist_pk_list.append(each.playlist_id)

            qst = get_playlists(playlist_pk_list).distinct()

            if settings.ORGANIZE_BY == 'likes':
                qst = sort_playlists_by_likes(qst)
            elif settings.ORGANIZE_BY == 'plays':
                qst = sort_playlists_by_plays(qst)

        return Page(qst, args[1], args[2], **kwargs)


class EntityListPagination(PageNumberPagination):
    """
    Overrides the class PageNumberPagination so that certain parameters could be set.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class SearchListPagination(EntityListPagination):
    """
    Overrides the class PageNumberPagination so that certain parameters could be set.
    """
    django_paginator_class = SearchPaginator
