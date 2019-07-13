from uwsgi_tasks import task, TaskExecutor, timer

from .redmine import Redmine


def __redmine_data_update():
    r = Redmine()
    r.import_tasks()
    r.import_month_stats()

    r.end()


@task(executor=TaskExecutor.SPOOLER, retry_count=1, retry_timeout=5)
def redmine_data_update():
    __redmine_data_update()


@timer(seconds=60*5)
def export_data(signal_number):
    __redmine_data_update()
