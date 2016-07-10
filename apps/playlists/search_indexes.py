from haystack import indexes

from .models import Tag


class TagIndex(indexes.SearchIndex, indexes.Indexable):

    """
    This class is responsible for indexing the Tag model on the AWS elastic search instance.
    The configuration settings are in settings.py for the AWS instance.

    Note: For updating the index run the management command: python manage.py update_index
    """

    text = indexes.NgramField(document=True, use_template=True)
    tag_name = indexes.CharField(model_attr='tag_name')

    def get_model(self):
        return Tag

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
