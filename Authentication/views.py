from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import UserAccount
from .serializers import UserAccountSerializer, UserSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    """
    REST view that allows to retrieve and edit account details
    """
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
