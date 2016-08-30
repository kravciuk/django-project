from __future__ import absolute_import
from .celery import app as celery_app

from uwsgi_tasks import django_setup

django_setup()
