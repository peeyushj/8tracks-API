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

        I pick up primary keys of the searchResult objects which are infact the primary keys of objects
        in the model. I do a filter based on primary keys that gives all the objects in a single MySQL query.
        """

        entity_pks = []
        entity_list = []

        for each in args[0]:
            entity_pks.append(each.pk)

        if len(entity_pks) > 0:
            # Get the model involved in the search
            model = args[0][0].model

            # Corresponding SQL statement to arrange queryset data based on primary key values:
            # SELECT * FROM theme ORDER BY FIELD(`id`, 10, 2, 1). Check out this:
            # http://blog.mathieu-leplatre.info/django-create-a-queryset-from-a-list-preserving-order.html

            # Using the same logic in ORM:
            ordering = 'FIELD(`tag_id`, %s)' % ','.join(str(id) for id in entity_pks)

            # Get the required tag elements
            entity_list = model.objects.filter(pk__in=entity_pks).extra(
                select={'ordering': ordering}, order_by=('ordering',))

            # Get the required models of playlists
            tag_pk_list = []
            for each in entity_list:
                tag_pk_list.append(each.tag_id)

            qst = get_playlists(tag_pk_list).distinct()

            if settings.ORGANIZE_BY == 'likes':
                qst = sort_playlists_by_likes(qst)
            elif settings.ORGANIZE_BY == 'plays':
                qst = sort_playlists_by_plays(qst)

        return Page(qst, args[1], args[2], **kwargs)


class EntityListPagination(PageNumberPagination):
    """
    Overrides the class PageNumberPagination so that certain parameters could
    be set.
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class SearchListPagination(EntityListPagination):
    """
    Overrides the class PageNumberPagination so that certain parameters could
    be set.
    """

    django_paginator_class = SearchPaginator
