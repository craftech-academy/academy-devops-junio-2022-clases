
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status



class ApiTestsBase(APITestCase):
    base_url_register = reverse("api:register-list")
    base_url_login = reverse("api:login-list")
    base_url_logout = reverse("api:logout-list")
    base_url_check_session = reverse("api:check-session-list")

    data_register = {"username": "admin", "password": "admin", "email": "admin@test.com"}
    data_login = {"password": "admin", "email": "admin@test.com"}
    data_wrong_login = {"password": "none", "email": "none@test.com"}


    def user_register(self):
        response = self.client.post(
            f"{self.base_url_register}", data=self.data_register
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        self.assertEqual(response_data["success"], True)