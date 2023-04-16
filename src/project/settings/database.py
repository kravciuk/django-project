# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import os
from .base import VAR_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(VAR_DIR, 'local.db'),
        # "HOST": 'localhost',
        # 'NAME': '',
        # 'USER': '',
        # 'PASSWORD': '',
    }
}

CONN_MAX_AGE = 60
