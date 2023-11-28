"""URL Configuration."""
from django.contrib import admin
from django.urls import include, path

BASE_VIEW_NAME = "chat"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", include("apps.chat.urls")),
    path("", include("apps.main.urls")),
]
