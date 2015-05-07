from django.contrib.auth.models import User

from rest_framework import serializers

from .models import UserAccount


class UserAccountSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for the UserAccount class"
    class Meta:
        model = UserAccount
        fields = ['user', 'real_name', 'country', 'phone']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

