from django_components import component

from apps.chat.models import Chat


@component.register("chat-sidebar")
class ChatSidebar(component.Component):
    template_name = "chat/chat-sidebar/chat-sidebar.html"

    def get_context_data(self, chat: Chat | None = None):
        return {
            "chats": Chat.objects.all(),
            "selected_chat": chat,
        }

    class Media:
        css = "chat/chat-sidebar/chat-sidebar.css"
        js = "chat/chat-sidebar/chat-sidebar.js"
