from django.test import TestCase

import TwitterAPI
from unittest.mock import patch

from .services import (_search_feeds_for_topic,
                      _search_latest_news_for_feed)
# Create your tests here.

class TwitterTestCase(TestCase):
    def test_retrieve_accounts(self):
#        patch('TwitterAPI.TwitterAPI.request', autospec=True).start()
        _search_feeds_for_topic("neuroscience")

    def test_retrieve_news(self):
#        patch('TwitterAPI.TwitterAPI.request', autospec=True).start()
        _search_feeds_for_topic("neuroscience")
        pass
