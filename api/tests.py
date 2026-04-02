from django.urls import reverse
from rest_framework.test import APITestCase
from django.utils import timezone
from accounts.models import User
from courses.models import Course, Category

class CourseAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="owner", password="pass123")
        self.category = Category.objects.create(name="API", slug="api")
        self.course = Course.objects.create(
            owner=self.user,
            category=self.category,
            title="API course",
            slug="api-course",
            description="Desc",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timezone.timedelta(days=1)).date(),
            price=0,
            is_published=True,
        )

    def test_list_courses(self):
        url = reverse("api-courses-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_course_requires_auth(self):
        url = reverse("api-courses-list")
        response = self.client.post(url, {
            "title": "New",
            "slug": "new",
            "description": "Desc",
            "start_date": timezone.now().date(),
            "end_date": (timezone.now() + timezone.timedelta(days=1)).date(),
            "price": 10,
            "is_published": True,
        })
        self.assertEqual(response.status_code, 401)
