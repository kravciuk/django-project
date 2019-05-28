# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.conf.urls import include, url
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',
        permission_required('is_superuser')(TemplateView.as_view(template_name='homepage/index.html')),
        name="homepage"),
]
