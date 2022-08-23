from rest_framework import serializers
from main.models import *


class TopicQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicQuery
        fields = ['instance_id', 'filter_id', 'topic_id', 'query_url']