from django.test import TestCase
from django.urls import reverse
from .models import User, Profile

class RegistrationTests(TestCase):
    def test_user_registration_creates_profile(self):
        response = self.client.post(reverse("accounts:register"), {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
            "is_instructor": True,
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username="testuser")
        self.assertTrue(Profile.objects.filter(user=user).exists())
        self.assertTrue(user.is_instructor)

    def test_duplicate_email_not_allowed(self):
        User.objects.create_user(username="u1", email="test@example.com", password="pass123")
        response = self.client.post(reverse("accounts:register"), {
            "username": "u2",
            "email": "test@example.com",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
            "is_instructor": False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "email", "This email is already registered.")


class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="loginuser", password="pass123")

    def test_login_success(self):
        response = self.client.post(reverse("accounts:login"), {
            "username": "loginuser",
            "password": "pass123",
        })
        self.assertEqual(response.status_code, 302)

    def test_profile_requires_login(self):
        response = self.client.get(reverse("accounts:profile_detail", args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
