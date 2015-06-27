from django.test import TestCase

from model_mommy import mommy

from .models import (Feed,
                     New,
                     Topic)
from .serializers import (FeedSerializer,
                          NewSerializer,
                          TopicSerializer)

# Create your tests here.

class FeedSerializerTestCase(TestCase):
    def test_feed_serializer(self):
        feed = mommy.prepare(Feed)
        serializer = FeedSerializer(feed)
        self.assertEqual(serializer.data, {
            "name": feed.name,
            "created": feed.created,
            "news": []
        })

    def test_feed_data_serializer(self):
        data = {
            "name": "F1",
            "created": None,
            "news": []
        }
        serializer = FeedSerializer(data=data)
        self.assertTrue(serializer.is_valid())


class NewSerializerTestCase(TestCase):
    def test_new_serializer(self):
        feed = mommy.make(Feed)
        url = "http://localhost:9000/v1/new/{}".format(feed.pk)
        new = mommy.prepare(New, account=url)
        serializer = FeedSerializer(new)
        self.assertEqual(serializer.data, {
            "account": new.account,
            "text": new.text,
            "date_added": new.date_added,
            "date_written": new.date_written
        })

    def test_new_data_serializer(self):
        data = {
            "text": "T1",
            "date_added": None,
            "date_written": None
        }
        serializer = NewSerializer(data=data)
        self.assertTrue(serializer.is_valid())


class TopicSerializerTestCase(TestCase):
    def test_topic_serializer(self):
        topic = mommy.prepare(Topic)
        serializer = TopicSerializer(topic)
        self.assertEqual(serializer.data, {
            "name": topic.name,
            "feeds": [],
            "created": topic.created,
            "last_access": topic.last_access
        })

#    def test_topic_data_serializer(self):
#        data = {
#        }
#        serializer = FeedSerializer(data=data)
#        self.assertTrue(serializer.is_valid())
