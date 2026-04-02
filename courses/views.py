from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course, Lesson
from .forms import CourseForm, LessonForm

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        qs = Course.objects.filter(is_published=True)
        category_slug = self.request.GET.get("category")
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class CourseDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/course_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("courses:course_list")


class LessonCreateView(LoginRequiredMixin, OwnerRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "courses/course_form.html"

    def form_valid(self, form):
        course = Course.objects.get(pk=self.kwargs["course_pk"])
        form.instance.course = course
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.course.get_absolute_url()
