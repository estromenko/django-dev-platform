from django.conf import settings
from django.contrib.auth import get_user_model
from django_components import component

User = get_user_model()


@component.register("header")
class Header(component.Component):
    template_name = "core/header/header.html"

    def get_context_data(self, user: User | None = None, site_name: str = ""):
        return {
            "user": user,
            "site_name": site_name,
            "apps": settings.APPS_IN_HEADER,
        }

    class Media:
        css = "core/header/header.css"
