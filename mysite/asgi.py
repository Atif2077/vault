import os

# 1️⃣ Set settings module FIRST
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  # replace mysite with your project name

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import django

# 2️⃣ Setup Django
django.setup()

# 3️⃣ Now imports that use Django (like routing or consumers)
from chat.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
