# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.db import models
from django.utils.translation import ugettext_lazy as _

from vu.abstract.models import BaseWithUser

from logging import getLogger
log = getLogger(__name__)


class Group(BaseWithUser):
    name = models.CharField(_(u'Name'), max_length=128)

    class Meta:
        verbose_name = _(u'Group')
        verbose_name_plural = _(u'Groups')

    def __str__(self):
        return str(self.pk)


class Event(BaseWithUser):
    group = models.ForeignKey(_(u'Group'), blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(_(u'Title'), max_length=256)
    description = models.TextField(_(u'Description'))
    date = models.DateTimeField(_(u'Date'), db_index=True)
    color = models.CharField(_(u'Color'), max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Event')

    def __str__(self):
        return str(self.pk)


class Drug(BaseWithUser):
    name = models.CharField(_(u'Name'), max_length=128)

    class Meta:
        verbose_name = _(u'Drug')
        verbose_name_plural = _(u'Drugs')

    def __str__(self):
        return str(self.pk)


class Hipertonic(BaseWithUser):
    drug = models.ForeignKey(Drug, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(_(u'Date'), db_index=True)
    sad = models.PositiveIntegerField(_(u'Sad'), default=0)
    dad = models.PositiveIntegerField(_(u'Dad'), default=0)
    pulse = models.PositiveIntegerField(_(u'Pulse'), default=0)
    comment = models.TextField(_(u'Comment'))

    class Meta:
        verbose_name = _(u'Record')
        verbose_name_plural = _(u'Records')

    def __str__(self):
        return str(self.pk)
