from django.db import models
from django.conf import settings
from courses.models import Course

User = settings.AUTH_USER_MODEL

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    progress = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} in {self.course}"
