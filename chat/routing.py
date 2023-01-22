from channels.auth import AuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/socket-server/',consumer.ChatConsumer.as_asgi())
]