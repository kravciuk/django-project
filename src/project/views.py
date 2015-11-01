# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404


def error404(request):
    context = {
        'title': 'Page not found',
        'text': 'Page not found',
    }

    return render(request, '404.html', context, status=404)


def index_page(request):
    context = {
        'title': 'Index page',
        'text': 'Django project started',
    }

    return render(request, 'index.html', context)
