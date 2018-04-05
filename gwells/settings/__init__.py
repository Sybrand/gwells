"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
import logging.config
from pathlib import Path

from gwells import database
from gwells.settings.base import get_env_variable

BASE_DIR = str(Path(__file__).parents[2])


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is provided via an environment variable in OpenShift
# safe value used for development when DJANGO_SECRET_KEY might not be set:
# '9e4@&tw46$l31)zrqe3wi+-slqm(ruvz&se0^%9#6(_w3ui!c0'
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY', '7e4@&tw46$l31)zrqe3wi+-slqm(ruvz&se0^%9#6(_w3ui!c0')

# Security Settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = get_env_variable('SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = get_env_variable('CSRF_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DJANGO_DEBUG', 'False') == 'True'

# Controls availability of the data entry functionality
ENABLE_DATA_ENTRY = get_env_variable('ENABLE_DATA_ENTRY', 'False') == 'True'

# Controls availability of Google Analytics
ENABLE_GOOGLE_ANALYTICS = get_env_variable('ENABLE_GOOGLE_ANALYTICS', 'False') == 'True'

# Additional Documents Feature Flag
ENABLE_ADDITIONAL_DOCUMENTS = get_env_variable('ENABLE_ADDITIONAL_DOCUMENTS', 'False') == 'True'

# Controls app context
APP_CONTEXT_ROOT = get_env_variable('APP_CONTEXT_ROOT', 'gwells')

FIXTURES_DIR = '/'.join([BASE_DIR, APP_CONTEXT_ROOT, 'fixtures'])

# Fixtures dirs
FIXTURES_DIRS = [FIXTURES_DIR]

# django-settings-export lets us make these variables available in the templates.
# This eleminate the need for setting the context for each and every view.
SETTINGS_EXPORT = [
    'ENABLE_DATA_ENTRY',            # To temporarily disable report submissions
    'ENABLE_GOOGLE_ANALYTICS',      # This is only enabled for production
    'ENABLE_ADDITIONAL_DOCUMENTS',  # To temporarily disable additional documents feature
    'APP_CONTEXT_ROOT',             # This allows for moving the app around without code changes
    'FIXTURES_DIRS'
]

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django.contrib.postgres',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'gwells',
    'crispy_forms',
    'formtools',
    'registries',
    'django_nose',
    'webpack_loader',
    'django_filters',
)

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'gwells.middleware.GWellsRequestParsingMiddleware',
)

ROOT_URLCONF = 'gwells.urls'
INTERNAL_IPS = '127.0.0.1'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': database.config()
}

# Re-use database connections, leave connection alive for 5 mimutes
CONN_MAX_AGE = 120

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

if APP_CONTEXT_ROOT:
    STATIC_URL = '/' + APP_CONTEXT_ROOT + '/static/'
else:
    STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'staticfiles')
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

DRF_RENDERERS = ['rest_framework.renderers.JSONRenderer', ]
# Turn on browsable API if "DEBUG" set
if DEBUG:
    DRF_RENDERERS.append('rest_framework.renderers.BrowsableAPIRenderer')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DRF_RENDERERS,
    'DEFAULT_PERMISSION_CLASSES': (
        'registries.permissions.IsAdminOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100000/hour',
        'user': '200000/hour'
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}
LOGIN_URL = '/gwells/accounts/login/'
LOGIN_REDIRECT_URL = '/gwells/search'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# matches subdomains of gov.bc.ca
CORS_ORIGIN_REGEX_WHITELIST = (r'^(?:https?:\/\/)?(?:\w+\.)*gov\.bc\.ca$',)
