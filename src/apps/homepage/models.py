# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.db import models
from django.utils.translation import ugettext_lazy as _

LABEL_CSS_CHOICE = (
    ('label_echo_blue', 'label_echo_blue'),
    ('label_dandelion', 'label_dandelion'),
    ('label_waikawa_grey', 'label_waikawa_grey'),
    ('label_tahuna_sands', 'label_tahuna_sands'),
    ('label_carmine', 'label_carmine'),
    ('label_kelly_green', 'label_kelly_green'),
    ('label_boulder', 'label_boulder'),
    ('label_fuchsia_pink', 'label_fuchsia_pink'),
    ('label_corious_blue', 'label_corious_blue'),
    ('label_biloba_flowere', 'label_biloba_flowere'),
    ('label_mona_lisa', 'label_mona_lisa'),
    ('label_neurtal_green', 'label_neurtal_green'),
    ('label_red_orange', 'label_red_orange'),
    ('label_hot_toddy', 'label_hot_toddy'),
    ('label_bright_sun', 'label_bright_sun'),
    ('label_regent_st_blue', 'label_regent_st_blue'),
    ('label_french_pass', 'label_french_pass'),
)


class RedmineTasks(models.Model):
    project = models.CharField(_(u'Project'), max_length=255)
    task = models.CharField(_(u'Task'), max_length=255)
    task_id = models.IntegerField(_(u'Task ID'))
    date = models.DateField(_(u'Date'))

    def __str__(self):
        return self.task

    class Meta(object):
        verbose_name = u'Задача'
        verbose_name_plural = u'Задачи'


class RedmineMonthStats(models.Model):
    date = models.DateField(_(u'Date'))
    hours = models.DecimalField(_(u'Hours'), default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s - %s" % (self.date, self.hours)

    class Meta(object):
        verbose_name = u'Время'
        verbose_name_plural = u'Время'


class HomepageLinkGroup(models.Model):
    name = models.CharField(u'Название', max_length=30)
    css_style = models.CharField(u'Css стиль', max_length=30, default=None, blank=True)
    css_class = models.CharField(u'Css класс', max_length=30, default=None, blank=True, choices=LABEL_CSS_CHOICE)
    hidden = models.BooleanField(u'Спрятать', default=False)
    _order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ('_order',)
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class HomepageLink(models.Model):
    group = models.ForeignKey(HomepageLinkGroup, verbose_name=u'Группа', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(u'Название', max_length=30)
    url = models.CharField(u'Ссылка', max_length=255)
    hidden = models.BooleanField(u'Спрятать', default=False)
    _order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ('_order',)
        verbose_name = u'Ссылка'
        verbose_name_plural = u'Ссылки'


class HomepageRegistrar(models.Model):
    name = models.CharField(u'Название', max_length=25, default='')
    url = models.CharField(u'Ссылка', max_length=255, default='')
    login_url = models.CharField(u'Ссылка входа', max_length=255, default=None, blank=True)
    affiliate_url = models.CharField(u'Партнерская ссылка', max_length=255, default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = u'Регистратор'
        verbose_name_plural = u'Регистраторы'


class HomepageDomains(models.Model):
    name = models.CharField(u'Название', max_length=25)
    registrar = models.ForeignKey(HomepageRegistrar, verbose_name=u'Регистратор', on_delete=models.SET_NULL, blank=True, null=True)
    url = models.CharField(u'Ссылка', max_length=255, default=None, blank=True)
    expired = models.DateField(u'Expired', default='2000-01-01')

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = u'Домен'
        verbose_name_plural = u'Домены'
