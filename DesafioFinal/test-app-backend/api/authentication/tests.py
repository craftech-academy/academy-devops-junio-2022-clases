from django.urls import reverse
from api.base.tests import ApiTestsBase
from rest_framework import status


class AuthenticationTest(ApiTestsBase):
    


    def test_login(self):
        self.user_register()
        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["success"], True)

    def test_logout(self):
        # Login to retrieve token
        self.user_register()
        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        response_data = response.json()

        token = response_data["token"]

        self.client.credentials(HTTP_AUTHORIZATION=token)

        # Logout

        response = self.client.post(f"{self.base_url_logout}", data={"token": token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["success"], True)

    def test_check_session(self):
        # Login to retrieve token
        self.user_register()
        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        response_data = response.json()
        token = response_data["token"]

        self.client.credentials(HTTP_AUTHORIZATION=token)

        # Check session
        response = self.client.post(f"{self.base_url_check_session}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data["success"], True)
