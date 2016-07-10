from __future__ import absolute_import, unicode_literals

import logging

from rest_framework import serializers

logger = logging.getLogger('apps.logs')


class SearchManagementCmdSerializer(serializers.Serializer):
    """This serializer handles running of management command within the `search` app"""

    command_ran = serializers.BooleanField(required=False, read_only=True)

    class Meta:
        fields = ('command_ran', )
