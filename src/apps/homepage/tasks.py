from .redmine import Redmine


def redmine_data_update():
    r = Redmine()
    r.import_tasks()
    r.import_month_stats()

    r.end()
