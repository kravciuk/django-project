# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

import csv
import pickle
import lxml.html

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from vcms.share.models import Share


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        file_path = '/mnt/hgfs/www/Xtube-Embed-Videos-Dump.csv'
        user = get_user_model().objects.filter(pk=1).get()
        with open(file_path, 'r') as fp:
            reader = csv.reader(fp, delimiter='|')

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

                # print(pickle.dumps(data))

                obj = Share(
                    user=user,
                    url=data['iframe'],
                    title=data['title'],
                    personal=True,
                )
                obj.save()
                obj.tags.add(*data['tags'])

                return

    def get_url(self, line):
        dom = lxml.html.fromstring(line)
        for link in dom.xpath('//iframe/@src'):
            return link
