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

ADMINS = (
    ('troll', 'chebusun@gmail.com'),
)

EMAIL_HOST = 'smtp.gmail.com'

# Do not use suggested 465 port for google SMTP. See
# https://code.djangoproject.com/ticket/9575
EMAIL_PORT = 587
EMAIL_HOST_USER = 'chebusun@gmail.com'
EMAIL_HOST_PASSWORD = 'H7IYrkL3SktM>4=1.cBS{07`'
EMAIL_USE_TLS = True

SERVER_EMAIL = 'django@my-domain.com'

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
    'django_nose',  # alleviate test running
    # provides reCAPTCHA field (https://github.com/praekelt/django-recaptcha)
    'captcha',
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

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}

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

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },

    }
}
