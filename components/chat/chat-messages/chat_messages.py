from django.contrib.auth import get_user_model
from django_components import component

from apps.chat.models import Chat, Message

User = get_user_model()


@component.register("chat-messages")
class ChatMessages(component.Component):
    template_name = "chat/chat-messages/chat-messages.html"

    def get_context_data(self, chat: Chat | None, user: User):
        return {
            "chat": chat,
            "messages": Message.objects.filter(chat_id=chat.id if chat else None),
            "user": user,
        }

    class Media:
        css = "chat/chat-messages/chat-messages.css"
        js = "chat/chat-messages/chat-messages.js"
