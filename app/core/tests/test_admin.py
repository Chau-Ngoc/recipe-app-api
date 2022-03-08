from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestAdminSite(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = get_user_model().objects.create_superuser(
            email="admin@gmail.com",
            password="123456789admin",
        )
        self.client.force_login(self.superuser)
        self.user = get_user_model().objects.create_user(
            email="user@gmail.com",
            password="123456789user",
            first_name="first name",
            last_name="last name",
        )

    def test_list_all_users(self):
        """Test that all users are listed on the users page."""
        url = reverse("admin:core_user_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the edit-user page works."""
        url = reverse("admin:core_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create-user page works."""
        url = reverse("admin:core_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
