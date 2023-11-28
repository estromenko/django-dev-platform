from django.contrib import admin

from apps.chat import models


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
