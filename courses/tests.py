from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from accounts.models import User
from .models import Course, Category

class CourseTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="owner", password="pass123")
        self.category = Category.objects.create(name="Test", slug="test")

    def test_course_create_view_requires_login(self):
        response = self.client.get(reverse("courses:course_create"))
        self.assertEqual(response.status_code, 302)

    def test_owner_can_create_course(self):
        self.client.login(username="owner", password="pass123")
        response = self.client.post(reverse("courses:course_create"), {
            "title": "My course",
            "slug": "my-course",
            "description": "Desc",
            "category": self.category.pk,
            "start_date": timezone.now().date(),
            "end_date": (timezone.now() + timezone.timedelta(days=1)).date(),
            "price": 10,
            "is_published": True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Course.objects.filter(slug="my-course").exists())

    def test_course_list_shows_published_only(self):
        Course.objects.create(
            owner=self.user,
            category=self.category,
            title="Unpublished",
            slug="unpub",
            description="Desc",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timezone.timedelta(days=1)).date(),
            price=0,
            is_published=False,
        )
        Course.objects.create(
            owner=self.user,
            category=self.category,
            title="Published",
            slug="pub",
            description="Desc",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timezone.timedelta(days=1)).date(),
            price=0,
            is_published=True,
        )
        response = self.client.get(reverse("courses:course_list"))
        self.assertContains(response, "Published")
        self.assertNotContains(response, "Unpublished")
