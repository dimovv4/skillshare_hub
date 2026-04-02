from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("create/", CourseCreateView.as_view(), name="course_create"),
    path("<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
    path("<slug:slug>/edit/", CourseUpdateView.as_view(), name="course_update"),
    path("<slug:slug>/delete/", CourseDeleteView.as_view(), name="course_delete"),
]
