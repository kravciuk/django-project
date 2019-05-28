# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from .models import Example

from logging import getLogger
log = getLogger(__name__)


