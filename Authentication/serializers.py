from django.contrib.auth.models import User

from rest_framework import serializers

from .models import UserAccount


class UserAccountSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for the UserAccount class"
    class Meta:
        model = UserAccount
        fields = ['user', 'real_name', 'country', 'phone']


class UserAccountRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)
    real_name = serializers.CharField(max_length=200)
    country = serializers.CharField(max_length=200)
    phone = serializers.IntegerField()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

