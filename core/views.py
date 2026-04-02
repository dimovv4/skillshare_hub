from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from courses.models import Course

class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["courses"] = Course.objects.filter(is_published=True)[:6]
        return ctx


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx["my_courses"] = user.courses.all()
        ctx["my_enrollments"] = user.enrollments.select_related("course")
        return ctx


def custom_404(request, exception):
    from django.shortcuts import render
    return render(request, "404.html", status=404)


def custom_500(request):
    from django.shortcuts import render
    return render(request, "500.html", status=500)
