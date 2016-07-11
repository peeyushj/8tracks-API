"""
This is the service layer to perform the necessary transformation of data that is required from the
database
"""

from .models import PlayList


def get_playlist_by_tags(pk_list):
    """
    Gets the playlists objects from the database for all tags.
    """
    qst = PlayList.objects.filter(tags__tag_id__in=pk_list)
    return qst

def get_playlists(pk_list):
    """
    Gets the playlists objects from the database for given playlist ids.
    """
    qst = PlayList.objects.filter(playlist_id__in=pk_list)
    return qst


def sort_playlists_by_likes(qst):
    """
    sorts the playlists list by likes field.
    """
    qst = qst.order_by('-' + 'likes')
    return qst


def sort_playlists_by_plays(qst):
    """
    sorts the playlists list by plays field.
    """

    qst = qst.order_by('-' + 'plays')
    return qst
