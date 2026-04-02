from django.contrib import admin
from .models import Category, Course, Lesson

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "slug")

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "owner", "category", "is_published", "start_date", "end_date")
    list_filter = ("is_published", "category")
    inlines = [LessonInline]
