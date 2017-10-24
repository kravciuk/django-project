# -*- coding: utf-8 -*-
import os
import sys
import glob

BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
VAR_DIR = os.path.normpath(os.path.join(BASE_DIR, '../var'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '=75dq8^7#rj%s#d#n^!9uer=s0hfvyd+d&knbn!2q5y2y28uh6'

SITE_ID = 1
DEBUG = True

ALLOWED_HOSTS = ['localhost']
ALLOWED_IPS = ['127.0.0.1', '192.168/16']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'dbbackup',
    'rosetta',
    'django_extensions',

    'project',
    'example',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_ROOT = os.path.join(VAR_DIR, 'htdocs/static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(VAR_DIR, 'htdocs/media')
MEDIA_URL = '/media/'

from .logging import *
from .database import *
from .regional import *
from .additional import *
from .templates import *

LOCAL_MIDDLEWARE = ()
LOCAL_APPS = ()

from .local import *

MIDDLEWARE_CLASSES += LOCAL_MIDDLEWARE
INSTALLED_APPS += LOCAL_APPS

