from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Message

@shared_task
def send_message_notification(message_id):
    message = Message.objects.get(pk=message_id)
    subject = f"New message: {message.subject}"
    body = f"You received a new message from {message.sender.username}.\n\n{message.body}"
    recipient_email = message.recipient.email
    if recipient_email:
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, "DEFAULT_FROM_EMAIL") else "no-reply@example.com",
            [recipient_email],
            fail_silently=True,
        )
