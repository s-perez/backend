from django.contrib.auth.models import User
from django.http import QueryDict

import simplejson as json
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Authentication.models import UserAccount
from Twitter.services import program_feed_discovery
from .models import Topic, Feed, New
from .serializers import (TopicSerializer,
                          NewSerializer,
                          FeedSerializer)

def get_user_from_request(request):
    token = request.auth
    return User.objects.get(auth_token__key=token)

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
        user = get_user_from_request(self.request)
        print(user)
        return Topic.objects.filter(accounts__user=user)

class TopicSubscription(GenericAPIView):

    def post(self, request):
        user = get_user_from_request(self.request)
        if Topic.objects.filter(name=request.POST.get('name')).exists():
            topic = Topic.objects.get(name=request.POST.get('name'))
        else:
            topic = self._subscribe_topic(request.POST.get('name'))
        account = UserAccount.objects.get(user=user)
        account.topics.add(topic)
        return Response({
            'name':topic.name
        })
    def _subscribe_topic(self, name):
        topic = Topic(name=name)
        program_feed_discovery(topic.name)
        topic.save()
        return topic

    def delete(self, request):
        body = json.loads(request.body)
        user = get_user_from_request(self.request)
        account = UserAccount.objects.get(user=user)
        if Topic.objects.filter(name=body.get('name')).exists():
            topic = Topic.objects.get(name=body.get('name'))
            if account.topics.filter(name=body.get('name')).exists():
                account.topics.remove(topic.pk)
            return Response(status=200)
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

#    def get_queryset(self):
#        """
#        This view should return a list of all the topics
#        for the currently authenticated user.
#        """
#        user = self.request.user
#        topics = Topic.objects.filter(accounts__user=user)
#        return New.objects.filter(topic__in=topics).order_by('date_written')
