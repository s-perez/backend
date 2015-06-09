from django.contrib.auth import User

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Authentication.models import UserAccount
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

class TopicSubscription(GenericAPIView):

    serializer_class = TopicSerializer


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            pk = getattr(self.request.auth, "account", None).pk
            user = User.objects.get(pk=pk)
            if Topic.objects.filter(name=serializer.data.name).exists():
                topic = Topic.objects.get(name=serializer.data.name)

            else:
                topic = self._subscribe_topic(serializer.data)

            account = UserAccount.objects.get(user=user)
            account.topics.add(topic)
            return Response({
                'name':topic.name
            })
    def _subscribe_topic(self, validated_data):
        topic = Topic(name=validated_data['name'])
        program_feed_discovery(topic.name)
        topic.save()
        return topic

    def delete(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            pk = getattr(self.request.auth, "account", None).pk
            user = User.objects.get(pk=pk)
            account = UserAccount.objects.get(user=user)
            if Topic.objects.filter(name=serializer.data.name).exists():
                topic = Topic.objects.filter(name=serializer.data.name)
                account.topics.remove(topic)
                return Response(
                    {},
                    status=200
                )
            else:
                return Response(
                    {},
                    status=status.HTTP_400_BAD_REQUEST
                )

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