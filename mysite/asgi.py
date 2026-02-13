import os
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.management import call_command

from chat import routing  # import your chat routing.py

# 1️⃣ Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 2️⃣ Setup Django
django.setup()

# 3️⃣ Run migrations safely (optional)
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration error:", e)

# 4️⃣ ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
