
from django.urls import path
from chat.consumers import *

websocket_urlpatterns = [
    path('ws/chat/', ChatConcumer.as_asgi()),
]
