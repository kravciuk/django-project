# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from .tasks import example_task
from project.tasks import project_task

import logging as log


def view_task(request):
    example_task(10)
    project_task(5)
    return render(request, 'example/task.html', {
        'content': '',
    })
