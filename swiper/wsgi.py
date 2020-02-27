"""
WSGI config for swiper project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if "SWIPER_DOCKER" in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings_docker")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

application = get_wsgi_application()
