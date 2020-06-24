# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.views.generic import View, DetailView, UpdateView, TemplateView, CreateView, DeleteView, ListView


class AbstractDetailView(DetailView):
    template_name = ''

    def get_queryset(self):
        return super().get_queryset()
