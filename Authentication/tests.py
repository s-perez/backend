from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory

from model_mommy import mommy

from .models import UserAccount
from .serializers import UserAccountSerializer

# Create your tests here.

class UserAccountSerializerTestCase(TestCase):
    def test_serialization(self):
        user = User.objects.create_user('u1', 'u@backend.com', '*u1*')
        url = "http://testserver/v1/users/{}/".format(user.pk)
        userAccount = mommy.make(UserAccount, user=user, phone=666666666)
        request = RequestFactory().get("/v1/accounts/{}/".format(userAccount.pk))
        serializer = UserAccountSerializer(userAccount, context={"request": request})

        self.assertEqual(serializer.data,{
            "user": url,
            "real_name": userAccount.real_name,
            "country": userAccount.country,
            "phone": userAccount.phone,
            "topics": []
        })
