# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk'

import os
from settings import VAR_DIR

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'Europe/Vilnius'
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'

SECRET_KEY = 'bvhaviahivGbkjsf(jbkjggygsf0983535'

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['dev.domain.com']
ALLOWED_IPS = ['127.0.0.1', '192.168/16']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'ENGINE': 'django.db.backends.mysql',
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(VAR_DIR, 'database.db'),
#         "HOST": 'localhost',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#     }
# }

DEFAULT_FROM_EMAIL = 'noreply@domain.com'
DEFAULT_FROM_NAME = 'Site Owner'
DEFAULT_CONTACT_EMAIL = 'admin@domain.com'
