from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.ForeignKey(User, unique=True)
    real_name = models.CharField(max_length=200)
    country = models.CharField(max_length=210)
    phone = models.IntegerField(blank=True)


