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
            first_name="Chau",
            last_name="Le",
        )
