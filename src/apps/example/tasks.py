# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import time

from uwsgi_tasks import task, TaskExecutor

import logging as log


@task(executor=TaskExecutor.SPOOLER, retry_count=1, retry_timeout=5)
def example_task(delay=10):
    log.debug('Task "example_task" started.')
    time.sleep(delay)
    log.debug('Task "example_task" ended.')
