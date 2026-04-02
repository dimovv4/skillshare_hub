from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm
from .tasks import send_message_notification

class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "communications/inbox.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "communications/message_detail.html"
    context_object_name = "message"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.recipient == self.request.user and not obj.is_read:
            obj.is_read = True
            obj.save()
        return obj


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "communications/message_form.html"
    success_url = reverse_lazy("communications:inbox")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        response = super().form_valid(form)
        send_message_notification.delay(self.object.pk)
        return response
