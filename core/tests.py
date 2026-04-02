from django.test import TestCase
from django.urls import reverse
from accounts.models import User

class CoreViewsTests(TestCase):
    def test_home_page_accessible(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("core:dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_logged_in(self):
        user = User.objects.create_user(username="u", password="pass123")
        self.client.login(username="u", password="pass123")
        response = self.client.get(reverse("core:dashboard"))
        self.assertEqual(response.status_code, 200)
