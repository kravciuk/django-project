from __future__ import absolute_import

import time

from uwsgi_tasks import task, TaskExecutor

from celery import shared_task

import logging as log


@task(executor=TaskExecutor.SPOOLER, retry_count=1, retry_timeout=5)
def project_task(delay=10):
    log.debug('Task "project_task" started.')
    time.sleep(delay)
    log.debug('Task "project_task" ended.')

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
