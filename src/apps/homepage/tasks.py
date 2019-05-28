from uwsgi_tasks import task, TaskExecutor, timer

from .redmine import Redmine


@task(executor=TaskExecutor.SPOOLER, retry_count=1, retry_timeout=5)
def redmine_data_update():
    r = Redmine()
    r.import_tasks()
    r.import_month_stats()

    r.end()


@timer(seconds=60*5)
def export_data(signal_number):
    redmine_data_update()
