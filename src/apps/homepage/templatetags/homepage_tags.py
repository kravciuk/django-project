# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from datetime import date, timedelta

from django import template
from django.db.models import Sum

from homepage.models import HomepageDomains, HomepageLinkGroup, RedmineTasks, RedmineMonthStats
from homepage.tasks import redmine_data_update

register = template.Library()


@register.simple_tag()
def domain_list():
    result = []
    date_now = date.today()

    rs = HomepageDomains.objects.select_related().all()
    for rec in rs:
        day_diff = (rec.expired - date_now).days
        rec.diff = day_diff
        result.append(rec)

    return result


@register.simple_tag()
def links_cloud(group=None):
    return HomepageLinkGroup.objects.filter(hidden=False)


@register.simple_tag()
def redmine_tasks():
    redmine_data_update()
    return RedmineTasks.objects.filter().order_by('date')


@register.inclusion_tag('homepage/month_stats.html', takes_context=True)
def redmine_month_stats(context):
    _date = date.today()
    rs = RedmineMonthStats.objects.filter(
        date__year=_date.year,
        date__month=_date.month
    ).aggregate(total=Sum('hours'))
    this_month_spent = rs['total']

    _date = _date.replace(day=1) - timedelta(days=1)
    rs = RedmineMonthStats.objects.filter(
        date__year=_date.year,
        date__month=_date.month
    ).aggregate(total=Sum('hours'))
    previous_month_spent = rs['total']

    _date = date.today()
    days = (date.today()-date.today().replace(day=1)).days
    all_days = (_date + timedelta(days=x) for x in range(days))
    this_month_planned = sum(1 for day in all_days if day.weekday() < 5)*5



    return {
        'this_month_spent': this_month_spent,
        'previous_month_spent': previous_month_spent,
        'this_month_planned': this_month_planned,
    }
