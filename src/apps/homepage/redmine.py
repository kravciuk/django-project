# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import mysql.connector

import MySQLdb as _mysql
from datetime import datetime

from django.conf import settings
from django.db import close_old_connections
from .models import RedmineMonthStats, RedmineTasks

import logging
log = logging.getLogger('tasks')


class Redmine:

    def __init__(self):
        self.db = mysql.connector.connect(user=settings.REDMINE_DB_USER, password=settings.REDMINE_DB_PASS, host=settings.REDMINE_DB_HOST,
                                      database=settings.REDMINE_DB_NAME, use_pure=True, charset='utf8')
        self.cursor = self.db.cursor()

        close_old_connections()

    def end(self):
        self.db.close()

    def import_tasks(self):
        query = """SELECT
                p.name,
                i.*
            FROM
                issues as i ,
                projects as p
            WHERE
                i.assigned_to_id = 37 AND i.status_id NOT IN (9, 12, 10)
                AND i.created_on > DATE_ADD(NOW(), INTERVAL -90 DAY)
                AND p.id = i.project_id
            ORDER BY i.id DESC"""

        try:
            self.cursor.execute(query)
            rs = list(RedmineTasks.objects.filter().values_list('task_id', flat=True))
        except Exception as e:
            log.error('MySQL error: %s' % e)
            return

        for row in self.cursor:
            task_id = int(row[1])
            if task_id in rs:
                rs.remove(task_id)
            else:
                RedmineTasks(
                    date=row[14],
                    project=row[0],
                    task=row[4],
                    task_id=row[1]
                ).save()

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

        self.cursor.execute(query)
        for row in self.cursor:
            obj, created = RedmineMonthStats.objects.get_or_create(
                date=_date
            )
            obj.hours = row[0]
            obj.save()
