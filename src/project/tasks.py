from __future__ import absolute_import

import time
from django.conf import settings
try:
    from uwsgidecorators import cron, spool, timer
except:
    print('UWSGI not available, use fake tasks')
    from vu.uwsgi_fake_decorators import cron, spool, timer

from logging import getLogger
log = getLogger(__name__)

# @timer(600, target='spooler')
# def timer_update_redmine_data(signum):
#     from homepage.tasks import redmine_data_update
#     redmine_data_update()

@spool
def task_update_redmine_data(*args, **kwargs):
    from homepage.tasks import redmine_data_update
    try:
        redmine_data_update()
    except Exception as e:
        log.error(e, exc_info=True)


@cron(20, 4, -1, -1, -1)
def backup():
    from django.core.management import execute_from_command_line
    argv = ['', 'dbbackup', '--compress', '--clean']
    execute_from_command_line(argv)


@spool
# @spool(pass_arguments=True)
def example_task(*args, **kwargs):
    from example.models import Example
    log.debug('Task "example_task" started.')
    # print(args)
    # print(kwargs)
    print(Example.objects.get(pk=kwargs['pk']))
    time.sleep(kwargs['delay'])
    log.debug('Task "example_task" ended.')
