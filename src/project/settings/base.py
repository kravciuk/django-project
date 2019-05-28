# -*- coding: utf-8 -*-
import os
import sys
import importlib
import re

BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
VAR_DIR = os.path.normpath(os.path.join(BASE_DIR, '../var'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '=75dq8^7#rj%s#d#n^!9uer=s0hfvyd+d&knbn!2q5y2y28uh6'

SITE_ID = 1
DEBUG = False

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
    'taggit',
    'taggit_autosuggest',
    'treebeard',
    'sitetree',
    'crispy_forms',
    'sekizai',
    'widget_tweaks',
    'adminsortable2',

    'ckeditor',
    'ckeditor_uploader',
    'embed_video',
    'vu.sendfile',

    'vu',
    'vcms',
    'vcms.content',
    'vcms.share',
    'vcms.comments',

    'homepage',
    # 'example',
    'project',

)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
from .vcms import *

LOCAL_MIDDLEWARE = ()
LOCAL_APPS = ()

rs = os.listdir(os.path.join(BASE_DIR, 'project/settings/local'))
for file_name in rs:
    match = re.search(r"(.*).py$", file_name, re.MULTILINE)
    if match:
        globals().update(importlib.import_module('project.settings.local.%s'%file_name[:-3]).__dict__)

MIDDLEWARE += LOCAL_MIDDLEWARE
INSTALLED_APPS += LOCAL_APPS

