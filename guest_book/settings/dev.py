from .base import *

INSTALLED_APPS += ('debug_toolbar',)

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'guest_book',
    'HOST': 'localhost',
    'USER': 'django_user',
    'PASSWORD': 'django_password',
    'PORT': '3306'
}

WSGI_APPLICATION = 'guest_book.wsgi.wsgi_dev.application'

