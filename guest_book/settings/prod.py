import dj_database_url
from .base import *

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allows to switch DEBUG setting in cloud (heroku)
# by running something like: heroku config:add DJANGO_DEBUG=true
DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))

TEMPLATE_DEBUG = DEBUG

# Allow all host headers
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'guest_book.wsgi.wsgi_prod.application'

DATABASES['default'] = dj_database_url.config()
