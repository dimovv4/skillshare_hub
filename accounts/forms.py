from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Required. We will never share your email.",
        error_messages={"required": "Please provide an email address."},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_instructor")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
        label="Username",
    )


class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, required=False, label="Username")
    email = forms.EmailField(disabled=True, required=False, label="Email")

    class Meta:
        model = Profile
        fields = ("bio", "website", "avatar")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["username"].initial = user.username
            self.fields["email"].initial = user.email
