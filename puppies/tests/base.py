from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase

from ..models import Puppy


class BaseTestCase(APITestCase):
    def setUp(self):

        self.client = APIClient()

        self.user = User.objects.create_superuser(
            username='test',
            email='test@test.com',
            password='testpassword'
        )
        self.assertEqual(self.user.is_active, 1, 'Active User')

        self.rambo = Puppy.objects.create(
            name='Rambo',
            age=1,
            breed='Gradane',
            colour='Yellow'
        )
        self.ricky = Puppy.objects.create(
            name='Ricky',
            age=3,
            breed='Bull Dog',
            colour='Black'
        )

        self.user_login = self.client.post('/api/token/', {
            'username': 'test',
            'password': 'testpassword',
        }, format='json')
        self.assertEqual(self.user_login.status_code, 200)
        self.token = self.user_login.data['access']
