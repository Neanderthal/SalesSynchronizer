# -*- coding: utf-8 -*-
import requests
import time
from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

from tttx.models import ShopProduct, ShopProductImages


@transaction.atomic
class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        counter = 0

        response = requests.get('https://api.vk.com/method/photos.get', params={
            'access_token': settings.VK_ACCESS_TOKEN,
            'owner_id': '-140432051',
            'album_id': '242677535',
            'rev': 1,
            'offset': 0,
            'count': 100,
            'v': '5.92'
        }).json()



        maxx = response['response']['count']
        items = response['response']['items']

        for index, item in enumerate(items):
            with open('log.txt', 'a') as f:
                print(index, maxx, item['id'], file=f)

            url = item['sizes'][-1]['url']
            text = item['text']
            filename = str(item['id'])

            print(response)

            r = requests.get(url)
            with open(filename + '.jpg', 'wb') as fp:
                fp.write(r.content)

            with open(filename + '.txt', 'w') as ft:
                ft.write(text)

            if index == maxx:
                break
            if items[-1] == item:
                response = requests.get('https://api.vk.com/method/photos.get', params={
                    'access_token': settings.VK_ACCESS_TOKEN,
                    'owner_id': '-140432051',
                    'album_id': '242677535',
                    'rev': 1,
                    'offset': 100,
                    'count': 101,
                    'v': '5.92'
                }).json()
                items.extend(response['response']['items'])
