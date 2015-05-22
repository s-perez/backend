
from rest_framework import serializers

from .models import Feed
from .models import Topic
from .models import New

class TopicSerializer (serializers.HyperlinkedModelSerializer):
    "Serializer for Topic class"
    class Meta:
        model = Topic
        fields = ['name','feeds','created','last_access']

class NewSerializer (serializers.HyperlinkedModelSerializer):
    "Serializer for the New class"
    class Meta:
        model = New
        fields = ['account','text', 'date_added','date_written']

class FeedSerializer (serializers.HyperlinkedModelSerializer):
    "Serializer for the Feed class"
    class Meta:
        model = Feed
        fields = ['name', 'created', 'news']