"""
ASGI config for my_learning_club project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator  # only hosts who have access to this websocket
from channels.auth import AuthMiddlewareStack
# from my_learning_club import routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_learning_club.settings')

# django_asgi_application = get_asgi_application()


# application = ProtocolTypeRouter({ 
#                                   'http':django_asgi_application,
#                                   'websocket':AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)))
#                                   })


import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
asgi_app=get_asgi_application()


from my_learning_club import routing
from channels.routing import ProtocolTypeRouter, URLRouter



application = ProtocolTypeRouter({
    "http": asgi_app,   
    'websocket':AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)))

})