# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import HomepageLinkGroup, HomepageLink, HomepageRegistrar, HomepageDomains


class HomepageLinkGroupAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name',)


class HomepageLinkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('group__name',)


class HomepageRegistrarAdmin(admin.ModelAdmin):
    list_display = ('name',)


class HomepageDomainsAdmin(admin.ModelAdmin):
    list_display = ('name', 'expired', 'registrar')


admin.site.register(HomepageLinkGroup, HomepageLinkGroupAdmin)
admin.site.register(HomepageLink, HomepageLinkAdmin)
admin.site.register(HomepageRegistrar, HomepageRegistrarAdmin)
admin.site.register(HomepageDomains, HomepageDomainsAdmin)

