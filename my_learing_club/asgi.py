"""
ASGI config for my_learing_club project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator  #only hosts who have access to this websocket
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_learing_club.settings')

django_asgi_application = get_asgi_application()

from chat import routing

application = ProtocolTypeRouter({ 
                                  'http':django_asgi_application,
                                  'websocket':AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)))

                                  })

