from django.urls import reverse
from api.base.tests import ApiTestsBase
from rest_framework import status


class UserViewSetTest(ApiTestsBase):
    base_edit_url = reverse("api:user-edit-list")
    base_url_login = reverse("api:login-list")



    def test_edit(self):

        # Login to retrieve token
        self.user_register()
        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        response_data = response.json()
        token = response_data["token"]
        user_id = response_data["user"]["_id"]

        self.client.credentials(HTTP_AUTHORIZATION=token)

        # Edit user

        data = {
            "email": "admin2@test.com",
            "userID": user_id,
        }

        response = self.client.post(f"{self.base_edit_url}", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        self.assertEqual(response_data["success"], True)
