from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileDetailView, ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]
