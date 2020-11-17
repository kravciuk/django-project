# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import uuid
from django.http import HttpResponse

from example.models import Example
from project.tasks import example_task

def view_task(request):
    obj, created = Example.objects.get_or_create(name=uuid.uuid4())
    print("Created object with id: %s" % obj.pk)
    example_task.spool(pk=obj.pk, delay=5)
    return HttpResponse('OK')
