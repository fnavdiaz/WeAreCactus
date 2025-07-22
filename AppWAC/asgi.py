"""
ASGI config for AppWAC project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.AppWAC.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppWAC.settings')

application = get_asgi_application()
