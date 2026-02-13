import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import django
from django.core.management import call_command

# 1️⃣ Set the settings module FIRST
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 2️⃣ Setup Django
django.setup()

# 3️⃣ Run migrations safely
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration error:", e)

# 4️⃣ ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
})
