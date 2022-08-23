from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from main.serializers import TopicQuerySerializer

from main.models import TopicQuery


class TopicQueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve topic information.
    """
    queryset = TopicQuery.objects.all()
    serializer_class = TopicQuerySerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = TopicQuery.objects.all()
        instance = self.request.query_params.get('instance', None)
        filter = self.request.query_params.get('filter', None)
        topic = self.request.query_params.get('topic', None)

        if instance is not None:
            queryset = queryset.filter(instance_id=instance)

        if filter is not None:
            queryset = queryset.filter(filter_id=filter)

        if topic is not None:
            queryset = queryset.filter(topic_id=topic)


        return queryset



