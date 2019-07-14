from __future__ import absolute_import

import time
from uwsgi_tasks import task, TaskExecutor, cron, timer
from django.conf import settings

import logging as log


@task(executor=TaskExecutor.SPOOLER, retry_count=1, retry_timeout=5)
def project_task(delay=10):
    log.debug('Task "project_task" started.')
    time.sleep(delay)
    log.debug('Task "project_task" ended.')


@cron(minute=20, hour=4)
def backup():
    from django.core.management import execute_from_command_line
    argv = ['', 'dbbackup', '--compress', '--clean']
    execute_from_command_line(argv)

