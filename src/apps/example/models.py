# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.db import models
from django.utils.translation import ugettext_lazy as _


from logging import getLogger
log = getLogger(__name__)


class ExampleManager(models.Manager):
    def aaa(self):
        print("AAA")


class Example(models.Model):
    name = models.CharField(_(u'Name'), max_length=64)

    objects = models.Manager()
    storage = ExampleManager()

    class Meta:
        verbose_name = _(u'Example')
        verbose_name_plural = _(u'Example')

    def __str__(self):
        return str(self.pk)
