from django.test import TestCase
from django.contrib.auth.models import User

from model_mommy import mommy

from .models import UserAccount
from .serializers import UserAccountSerializer

# Create your tests here.

#class UserAccountSerializerTestCase(TestCase):
#    def test_serialization(self):
#        user = User.objects.create(username="u1")
#        user.save()
#        userAccount = UserAccount(user=user)
#        serializer = UserAccountSerializer(data={
#            "user": userAccount.user,
#            "real_name": userAccount.real_name,
#            "country": userAccount.country,
#            "phone": userAccount.phone,
#            "topics": userAccount.topics
#        })
#        self.assertTrue(serializer.is_valid(), serializer.errors)
#        self.assertEqual(serializer.data,userAccount)
