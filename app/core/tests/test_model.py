from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating new user using their email address."""
        email = "test@GMAIL.COM"
        password = "123456789test"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertIsNotNone(user)
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_create_user_with_invalid_email(self):
        """Test creating new user with invalid email. Expecting an
        ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="", password="test123")

    def test_create_superuser(self):
        superuser = get_user_model().objects.create_superuser(
            email="superuser@gmail.com", password="test123"
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
