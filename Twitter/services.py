from backend.settings import TWITTER

import requests
from django_rq import job
from TwitterAPI import TwitterAPI


def _auth_twitter_api():
    return TwitterAPI(consumer_key=TWITTER['CONSUMER_KEY'],
                      consumer_secret=TWITTER['CONSUMER_SECRET'],
                      access_token_key=TWITTER['TOKEN_KEY'],
                      access_token_secret=TWITTER['TOKEN_SECRET'])


@job("high")
def _search_feeds_for_topic(topic):
    twitter = _auth_twitter_api()
    request = twitter.request('users/search', {'q': topic})
    ranked_users = {}
    for user in request:
        name = user.screen_name
        rating = user.followers / user.favourites
        ranked_users[name] = rating
        print(user)


@job("default")
def _search_latest_news_for_feed(feed):
    twitter = _auth_twitter_api()
    request = twitter.request('statuses/user_timeline', {"screen_name": feed})
    for new in request:
        print(new.text)


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

