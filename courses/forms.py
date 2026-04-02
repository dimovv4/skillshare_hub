from django import forms
from .models import Course, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ("owner", "students", "created_at")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Course title"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }
        help_texts = {
            "price": "Set 0 for a free course.",
        }

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "content", "order")

    def clean_order(self):
        order = self.cleaned_data["order"]
        if order == 0:
            raise forms.ValidationError("Order must be at least 1.")
        return order
