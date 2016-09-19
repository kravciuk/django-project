from __future__ import absolute_import

import time
from uwsgi_tasks import task, TaskExecutor

import logging as log


@task(executor=TaskExecutor.SPOOLER, retry_count=1, retry_timeout=5)
def project_task(delay=10):
    log.debug('Task "project_task" started.')
    time.sleep(delay)
    log.debug('Task "project_task" ended.')
