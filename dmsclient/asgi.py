import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import path
from scanmonitoring import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/files/", consumers.FileConsumer.as_asgi()),
        ])
    ),
})
