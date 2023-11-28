from django.urls import path

from apps.chat import views

urlpatterns = [
    path("", views.ChatView.as_view(), name="chat"),
    path("<int:chat_id>/", views.ChatView.as_view(), name="chat"),
    path(
        "<int:chat_id>/messages/",
        views.ChatMessagesView.as_view(),
        name="chat-messages",
    ),
    path(
        "<int:chat_id>/messages/<int:message_id>/",
        views.ChatMessagesView.as_view(),
        name="chat-message",
    ),
]
