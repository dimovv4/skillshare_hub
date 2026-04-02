from django.urls import path
from .views import EnrollmentListView, EnrollView

app_name = "enrollments"

urlpatterns = [
    path("", EnrollmentListView.as_view(), name="enrollment_list"),
    path("course/<slug:slug>/enroll/", EnrollView.as_view(), name="enroll"),
]
