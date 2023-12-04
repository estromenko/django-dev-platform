from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = "chat"

    def __str__(self) -> str:
        return self.name

    @property
    def image_placeholder_text(self):
        return self.name[0].upper()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    class Meta:
        db_table = "message"
        ordering = ("created_at",)

    def __str__(self) -> str:
        return f'({self.id}) {self.sender.username}: "{self.text}"'
