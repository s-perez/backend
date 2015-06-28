from django.test import TestCase
from django.test.client import RequestFactory

from datetime import datetime
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
        feed = Feed(name="F1")
        feed.save()
        url = "http://testserver/v1/feed/{}/".format(feed.pk)
        new = New(account=feed, text="Text1")
        new.save()
        request = RequestFactory().get("/v1/new/{}".format(new.pk))
        serializer = NewSerializer(new, context={"request": request})
        self.assertEqual(serializer.data, {
            "account": url,
            "text": new.text,
            "date_added": new.date_added.isoformat().replace('+00:00', 'Z'),
            "date_written": new.date_written.isoformat().replace('+00:00', 'Z')
        })


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
