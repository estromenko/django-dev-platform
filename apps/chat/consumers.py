import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.template.loader import render_to_string

from apps.chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = ""
    room_group_name = ""

    async def connect(self) -> None:
        self.room_name = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code) -> None:
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None) -> None:
        text_data_json = json.loads(text_data)
        message = text_data_json["text"]

        if not message:
            return

        message = await Message.objects.acreate(
            sender=self.scope["user"],
            chat_id=self.scope["url_route"]["kwargs"]["chat_id"],
            text=message,
        )

        response = render_to_string(
            "chat/includes/wrapper-message.html",
            {
                "message": message,
                "user": self.scope["user"],
            },
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "send_message", "message": response},
        )

    async def send_message(self, event):
        return await self.send(event["message"])
