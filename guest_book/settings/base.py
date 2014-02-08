"""
Django settings for guest_book project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8@@tvl_p*s+tpr@ed42fueig=5!j=(u8qfoz-s@nq5phourk6a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guest_book.apps.book',
    'south',
    'debug_toolbar',
    'django_nose',  # alleviate test running
    'captcha',  # tools for using reCAPTCHA
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'guest_book.urls'

WSGI_APPLICATION = 'guest_book.wsgi.wsgi_dev.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guest_book',
        'HOST': 'localhost',
        'USER': 'django_user',
        'PASSWORD': 'django_password',
        'PORT': '3306'
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

RECAPTCHA_PUBLIC_KEY = '6LexMO4SAAAAAGgTgpSWF_QcavxybjGZ4Hckhkhx'
RECAPTCHA_PRIVATE_KEY = '6LexMO4SAAAAAGjlBM46UJk3fwGzWTUSoLHVhR8j'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
