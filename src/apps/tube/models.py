# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.db import models
from django.utils.translation import ugettext_lazy as _

from logging import getLogger
log = getLogger(__name__)


class Example(models.Model):

    class Meta:
        verbose_name = _(u'Example')
        verbose_name_plural = _(u'Example')

    def __str__(self):
        return str(self.pk)
