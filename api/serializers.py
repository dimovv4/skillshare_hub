from rest_framework import serializers
from accounts.models import User, Profile
from courses.models import Course
from enrollments.models import Enrollment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("bio", "website", "avatar")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "is_instructor", "profile")


class CourseSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "start_date",
            "end_date",
            "price",
            "is_published",
            "owner",
        )


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ("id", "user", "course", "status", "progress", "created_at")
