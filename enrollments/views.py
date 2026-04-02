from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
from courses.models import Course
from .models import Enrollment

class EnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = "enrollments/enrollment_list.html"
    context_object_name = "enrollments"

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)


class EnrollView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=kwargs["slug"])
        Enrollment.objects.get_or_create(user=request.user, course=course)
        return redirect(course.get_absolute_url())
