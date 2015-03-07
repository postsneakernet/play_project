"""
WSGI config for play project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

# add project to path
sys.path.append('/home/play/web_dev/play_project/play')
# add virtualenv site-packages to path
sys.path.append('/home/play/.virtualenvs/play_project/lib/python3.4/site-packages/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "play.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
