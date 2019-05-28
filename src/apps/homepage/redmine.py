# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import MySQLdb as _mysql
from datetime import datetime

from django.conf import settings
from django.db import close_old_connections
from .models import RedmineMonthStats, RedmineTasks

import logging
log = logging.getLogger('tasks')


class Redmine:

    def __init__(self):
        self.db = _mysql.connect(host=settings.REDMINE_DB_HOST, db=settings.REDMINE_DB_NAME,
                                 user=settings.REDMINE_DB_USER, passwd=settings.REDMINE_DB_PASS, charset='utf8', init_command='SET NAMES UTF8')
        log.info('MySQL connection to redmine opened.')

        close_old_connections()

    def end(self):
        self.db.close()
        log.info('MySQL connection to redmine closed.')

    def import_tasks(self):
        query = """SELECT
                p.name,
                i.*
            FROM
                issues as i ,
                projects as p
            WHERE
                i.assigned_to_id = 37 AND i.status_id NOT IN (9, 12)
                AND i.created_on > DATE_ADD(NOW(), INTERVAL -90 DAY)
                AND p.id = i.project_id
            ORDER BY i.id DESC"""

        try:
            self.db.query(query)
            res = self.db.use_result()
            rs = list(RedmineTasks.objects.filter().values_list('task_id', flat=True))
        except Exception as e:
            log.error('MySQL error: %s' % e)
            return

        row = res.fetch_row()
        while row:
            task_id = int(row[0][1])
            if task_id in rs:
                rs.remove(task_id)
            else:
                task = RedmineTasks(
                    date=row[0][14],
                    project=row[0][0],
                    task=row[0][4],
                    task_id=row[0][1]
                ).save()

            row = res.fetch_row()

        RedmineTasks.objects.filter(task_id__in=rs).delete()

    def import_month_stats(self, date=None):
        _date = datetime.now() if date is None else date
        query = """SELECT
                SUM(hours), spent_on
            FROM
                time_entries
            WHERE
                user_id IN ('37')
                AND spent_on='%s'
            GROUP BY spent_on""" % _date.strftime("%Y-%m-%d")

        self.db.query(query)
        res = self.db.use_result()
        row = res.fetch_row()
        if row:
            obj, created = RedmineMonthStats.objects.get_or_create(
                date=_date
            )
            obj.hours = row[0][0]
            obj.save()
