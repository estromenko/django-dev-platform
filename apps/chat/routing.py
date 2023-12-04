from django.urls import re_path

from apps.chat import consumers

websocket_urlpatterns = [
    re_path(r"^chat/ws/(?P<chat_id>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
