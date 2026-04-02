from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from .models import Message

class MessageTests(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username="sender", password="pass123", email="s@example.com")
        self.recipient = User.objects.create_user(username="recipient", password="pass123", email="r@example.com")

    def test_inbox_requires_login(self):
        response = self.client.get(reverse("communications:inbox"))
        self.assertEqual(response.status_code, 302)

    def test_send_message(self):
        self.client.login(username="sender", password="pass123")
        response = self.client.post(reverse("communications:message_create"), {
            "recipient": self.recipient.pk,
            "subject": "Hello",
            "body": "Test message",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Message.objects.filter(subject="Hello").exists())

    def test_recipient_sees_message_in_inbox(self):
        msg = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            subject="Hi",
            body="Body",
        )
        self.client.login(username="recipient", password="pass123")
        response = self.client.get(reverse("communications:inbox"))
        self.assertContains(response, "Hi")
