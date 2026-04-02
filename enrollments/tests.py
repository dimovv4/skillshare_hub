from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from accounts.models import User
from courses.models import Course, Category
from .models import Enrollment

class EnrollmentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="student", password="pass123")
        self.owner = User.objects.create_user(username="owner", password="pass123")
        self.category = Category.objects.create(name="Cat", slug="cat")
        self.course = Course.objects.create(
            owner=self.owner,
            category=self.category,
            title="Course",
            slug="course",
            description="Desc",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timezone.timedelta(days=1)).date(),
            price=0,
            is_published=True,
        )

    def test_enrollment_requires_login(self):
        response = self.client.post(reverse("enrollments:enroll", args=[self.course.slug]))
        self.assertEqual(response.status_code, 302)

    def test_user_can_enroll(self):
        self.client.login(username="student", password="pass123")
        response = self.client.post(reverse("enrollments:enroll", args=[self.course.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Enrollment.objects.filter(user=self.user, course=self.course).exists())

    def test_enrollment_list_requires_login(self):
        response = self.client.get(reverse("enrollments:enrollment_list"))
        self.assertEqual(response.status_code, 302)
