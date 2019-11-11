# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.urls import path
from django.views.generic import TemplateView

app_name = 'tube'
urlpatterns = [
    path('', TemplateView.as_view(template_name='tube/index.html'), name="index"),
    path('view-<slug:slug>/', TemplateView.as_view(template_name='tube/view.html'), name="view_content"),
]
