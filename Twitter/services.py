import operator
import requests

from django_rq import job
from TwitterAPI import TwitterAPI

from backend.settings import TWITTER
from Topics.models import Feed, New, Topic

def _auth_twitter_api():
    return TwitterAPI(consumer_key=TWITTER['CONSUMER_KEY'],
                      consumer_secret=TWITTER['CONSUMER_SECRET'],
                      access_token_key=TWITTER['TOKEN_KEY'],
                      access_token_secret=TWITTER['TOKEN_SECRET'])


@job("high")
def _search_feeds_for_topic(topic):
    twitter = _auth_twitter_api()
    request = twitter.request('users/search', {'q': topic})
    ranked_feeds = {}
    for feed in request.json():
        name = feed['screen_name']
        rating = feed['followers_count']
        if feed["friends_count"] != 0:
            rating = rating / feed['friends_count']
        ranked_feeds[name] = rating
    sorted_feeds = sorted(ranked_feeds.items(), key=operator.itemgetter(1))
    parent_topic = Topic.objects.get_or_create(name=topic)[0]
    for feed in sorted_feeds[:5]:
        feed = Feed.objects.get_or_create(name=feed[0])[0]
        feed.save()
        feed.topics.add(parent_topic.pk)


@job("default")
def _search_latest_news_for_feed(feed):
    twitter = _auth_twitter_api()
    request = twitter.request('statuses/user_timeline', {"screen_name": feed})
    feed_object = Feed.objects.get(name=feed)
    for new in request:
        new_new = New(text=new['text'], account=feed_object)
        new_new.save()


def program_feed_discovery(topic):
    _search_feeds_for_topic.delay(topic)


def program_feed_discovery_bulk(topic_list):
    for topic in topic_list:
        program_feed_discovery(topic)


def program_news_download(feed):
    _search_latest_news_for_feed.delay(feed)

def program_news_download_bulk(feed_list):
    for feed in feed_list:
        program_news_download(feed)

