from __future__ import unicode_literals

from rest_framework import serializers

from .models import PlayList, Tag


class TagsListSerializer(serializers.ModelSerializer):

    """
    Gets the list of all tag instances in the system.
    """

    class Meta:
        model = Tag
        fields = ('tag_name', )


class NewTagPostSerializer(serializers.ModelSerializer):
    """This serializer handles the POST request to create a new tag"""

    tag_name = serializers.CharField()

    class Meta:
        model = Tag
        fields = ('tag_name', )
        read_only_fields = ('tag_id', )

    def save(self):
        """Overriding the default save method"""

        tag_name = self.validated_data['tag_name']

        tag_object = Tag.objects.create(
            tag_name=tag_name,
        )
        self.instance = tag_object
        return tag_object


class TagDetailSerializer(TagsListSerializer):
    pass


class UpdateTagSerializer(TagsListSerializer):
    pass


class PlaylistsListSerializer(serializers.HyperlinkedModelSerializer):

    """
    Gets the list of all PlayList instances in the system.
    """

    class Meta:
        model = PlayList
        fields = ('playlist_id', 'playlist_name', 'likes', 'plays')


class NewPlaylistPostSerializer(serializers.ModelSerializer):
    """This serializer handles the POST request to create a new playlist"""

    playlist_name = serializers.CharField()
    likes = serializers.IntegerField()
    plays = serializers.IntegerField()
    tags = TagDetailSerializer(read_only=True, many=True)

    class Meta:
        model = PlayList
        fields = ('playlist_name', 'likes', 'plays', 'tags')
        read_only_fields = ('playlist_id', )

    def save(self):
        """Overriding the default save method."""

        playlist_name = self.validated_data['playlist_name']
        likes = self.validated_data['likes']
        plays = self.validated_data['plays']

        playlist_object = PlayList.objects.create(
            playlist_name=playlist_name,
            likes=likes,
            plays=plays,
        )
        self.instance = playlist_object
        return playlist_object


class PlaylistDetailSerializer(PlaylistsListSerializer):
    pass


class UpdatePlaylistSerializer(serializers.ModelSerializer):

    """
    Serializer to update the playlist instance in the system.
    """    
    
    class Meta:
        model = PlayList
        fields = ('playlist_id', 'playlist_name', 'likes', 'plays')
