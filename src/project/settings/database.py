# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.mysql',
        "HOST": 'localhost',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}

CONN_MAX_AGE = 60
