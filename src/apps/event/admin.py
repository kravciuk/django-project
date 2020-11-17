# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Event, Group, Hipertonic, Drug

from logging import getLogger
log = getLogger(__name__)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    autocomplete_fields = []
