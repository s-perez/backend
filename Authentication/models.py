from django.db import models
from django.contrib.auth.models import User

from Topics.models import Topic

class UserAccount(models.Model):
    user = models.OneToOneField(User)
    real_name = models.CharField(max_length=200)
    country = models.CharField(max_length=210)
    phone = models.IntegerField(blank=True)
    topics = models.ManyToManyField(Topic, related_name="accounts")


