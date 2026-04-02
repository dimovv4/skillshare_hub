from django.urls import path
from .views import InboxView, MessageDetailView, MessageCreateView

app_name = "communications"

urlpatterns = [
    path("", InboxView.as_view(), name="inbox"),
    path("new/", MessageCreateView.as_view(), name="message_create"),
    path("<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
]
