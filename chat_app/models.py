from django.db import models

from user_app.models import CustomUser

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender_messages")
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="recipient_messages")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.email
