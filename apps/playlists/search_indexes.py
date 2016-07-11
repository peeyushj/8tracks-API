from haystack import indexes

from .models import PlayList

class PlayListIndex(indexes.SearchIndex, indexes.Indexable):

    """
    This class is responsible for indexing the Playlist model on the solr instance.
    Note: For updating the index run the management command: python manage.py update_index
    """

    text = indexes.NgramField(document=True, use_template=True)
    playlist_name = indexes.CharField(model_attr='playlist_name')
    plays = indexes.IntegerField(indexed=True, stored=True,model_attr='plays')
    tags = indexes.MultiValueField(indexed=True, stored=True, model_attr='tags', null=True)

    def get_model(self):
        return PlayList

    def prepare_tags(self, obj):
     return [tag.tag_name for tag in obj.tags.all()] or None

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
