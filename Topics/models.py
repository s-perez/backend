from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=75)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{0}".format(self.name)

class Topic(models.Model):
    name = models.CharField(max_length=75)
    feeds = models.ManyToManyField(Feed, related_name="topics")
    created = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{0}".format(self.name)


class New(models.Model):
    account = models.ForeignKey(Feed, related_name="news")
    text = models.CharField(max_length="200")
    date_added = models.DateTimeField(auto_now_add=True)
    date_written = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}: {1}".format(self.account.name, self.text)

