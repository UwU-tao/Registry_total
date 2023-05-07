from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CreateUserTestCase(APITestCase):

    # User - Create (Token auth - for API) 😊
    def test_registration(self):
        data = {"username": "branko", "first_name": "Branko", "password": "brankobranko"}
        response = self.client.post("/api/users/new/", data)
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['token'], token.key)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token = Token.objects.get(user__username='branko')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key) # token will be included in all requests - login alias

     # User - Login (Session based - for web browser) 😊
    def test_login(self):
        data = {"username": "leon", "password": "leonleon"}
        response = self.client.post("/api-auth/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)