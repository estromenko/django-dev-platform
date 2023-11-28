from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.chat.models import Chat, Message


class ChatView(LoginRequiredMixin, TemplateView):
    template_name = "chat/index.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        messages = Message.objects.none()
        chat_id = self.kwargs.get("chat_id")
        if chat_id:
            messages = Message.objects.filter(chat_id=chat_id)
        chat = Chat.objects.filter(id=chat_id).first()
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "chat": chat,
                "messages": messages,
                "user": self.request.user,
            }
        )
        return context


class ChatMessagesView(TemplateView):
    template_name = "chat/messages.html"
    model = Message

    def get_context_data(self, **kwargs):
        chat_id = self.kwargs.get("chat_id")
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "chat": Chat.objects.get(id=chat_id),
                "user": self.request.user,
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        chat_id = self.kwargs.get("chat_id")
        text = request.POST.get("text", "").strip()
        if text:
            Message.objects.create(text=text, sender=request.user, chat_id=chat_id)
        return self.render_to_response(self.get_context_data())

    def delete(self, request, *args, **kwargs):
        message_id = self.kwargs.get("message_id")
        Message.objects.get(id=message_id).delete()
        return self.render_to_response(self.get_context_data())
