# settings/production.py

from .local import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = "/home/play/public_html/media"
MEDIA_URL = '/~play/media/'
STATIC_URL = '/~play/static/'
