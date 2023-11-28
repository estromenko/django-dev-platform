from django_components import component

from apps.chat.models import Chat


@component.register("chat-page")
class ChatPage(component.Component):
    template_name = "chat/chat-page/chat-page.html"

    def get_context_data(self, chat: Chat | None = None):
        return {
            "chat": chat,
        }

    class Media:
        css = "chat/chat-page/chat-page.css"
