from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Topic, Feed, New
from .serializers import (TopicSerializer,
                          NewSerializer,
                          FeedSerializer)

class TopicViewSet (viewsets.ModelViewSet):
    """
    REST view that allows to retrieve topics from the logged user
    """
    serializer_class = TopicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the topics
        for the currently authenticated user.
        """
        user = self.request.user
        return Topic.objects.filter(accounts__user=user)

class FeedViewSet (viewsets.ModelViewSet):
    """
    REST view that allows to retrieve feeds from the logged user
    """
    serializer_class = FeedSerializer

    queryset = Feed.objects.all()


class NewViewSet (viewsets.ModelViewSet):
    """
    REST view that allows to retrieve news from the logged user
    """
    serializer_class = NewSerializer

    queryset = New.objects.all()