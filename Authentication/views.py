from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import UserAccount
from .serializers import (UserAccountSerializer,
                          UserAccountRegistrationSerializer,
                          UserSerializer)


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


class UserAccountRegistration(GenericAPIView):
    permission_classes = (
        AllowAny,
    )
    serializer_class = UserAccountRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            user = self._register_user_account(serializer.data)
            return Response({
                'email': user.email
            })

    def _register_user_account(self, validated_data):
        user = User(username=validated_data['email'],
                    email=validated_data['email'],
                    is_active=True)
        user.set_password(validated_data['password'])
        user.save()
        account = UserAccount(
            user=user,
            real_name=validated_data['real_name'],
            country=validated_data['country'],
            phone=validated_data['phone']
        )
        account.save()
        return user


