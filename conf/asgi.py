"""ASGI config for conf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import subprocess
import sys

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf import settings
from django.core.asgi import get_asgi_application

from apps.chat.routing import websocket_urlpatterns as chat_patterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        *chat_patterns,
                    ],
                ),
            ),
        ),
    },
)

if not settings.DEBUG:
    config_path = settings.BASE_DIR / "tailwind.config.js"
    input_file = settings.BASE_DIR / "apps/core/static/core/css/styles.css"
    output_file = settings.BASE_DIR / "dist/styles.css"
    command = f"tailwindcss -c {config_path} -i {input_file} -o {output_file} -w -p"
    subprocess.run(
        command.split(),
        shell=True,
        check=True,
        stderr=sys.stderr,
        stdout=sys.stdout,
    )
