from django_components import component

from apps.chat.models import Chat


@component.register("message-input")
class MessageInput(component.Component):
    template_name = "chat/message-input/message-input.html"

    def get_context_data(self, chat: Chat):
        return {
            "chat": chat,
        }

    class Media:
        css = "chat/message-input/message-input.css"
        js = "chat/message-input/message-input.js"
