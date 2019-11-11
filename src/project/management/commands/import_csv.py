# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import csv
import sys
import json
import lxml.html

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from vcms.share.models import Share
from vu.network import Download

class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        maxInt = sys.maxsize
        csv.field_size_limit(maxInt)
        print("Set CSV max size to %s from 131072" % maxInt)

        file_path = '/mnt/hgfs/www/Xtube-Embed-Videos-Dump.csv'
        user = get_user_model().objects.filter(pk=1).get()
        Share.objects.filter(id__gt=5).delete()
        with open(file_path, 'r', encoding='latin1') as fp:
            reader = csv.reader(fp, delimiter='|')

            i = 0
            total = 0
            for row in reader:
                data = {
                    'id': row[0],
                    'iframe': self.get_url(row[1]),
                    'url': row[2],
                    'thumbnail': row[3],
                    'thumbnails': row[4].split(','),
                    'title': row[5],
                    'tags': row[6].split(','),
                }

                obj = Share(
                    user=user,
                    url=data['iframe'],
                    title=data['title'],
                    personal=True,
                    json=json.dumps(data),
                )
                obj.save()
                obj.tags.add(*data['tags'])

                i += 1
                total += 1
                if (i % 50) == 0:
                    print(total)
                    i = 0

        print('Done')

    def get_url(self, line):
        dom = lxml.html.fromstring(line)
        for link in dom.xpath('//iframe/@src'):
            return link
