# -*- coding: utf-8 -*-
from datetime import datetime

import requests
import vk
from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

from tttx.models import ShopProduct, ShopProductImages, ShopProductParams


def update_date_changed(params_filter, product):
    date_changed = False
    if not product.edit_datetime:
        saved_date = datetime.now()
        product.edit_datetime = saved_date
        product.save()
    else:
        saved_date = product.edit_datetime
    if not params_filter.exists():
        product_param = ShopProductParams(
            product_id=product.id,
            name='saved_date',
            value=saved_date,
        )
        product_param.save()

        date_changed = True
    else:
        product_param = params_filter.get()
        if product_param.value == saved_date:

            date_changed = True
        else:
            product_param.value = saved_date
            product_param.save()

    return date_changed


def post_photo(caption, url):
    album_id = settings.VK_ALBUM_ID,
    group_id = settings.VK_GROUP_ID,

    # Получаем адрес сервера для загрузки фотографии
    response = requests.get(
        'https://api.vk.com/method/photos.getUploadServer', params={
            'access_token': settings.VK_ACCESS_TOKEN,
            'album_id': album_id,
            'group_id': group_id,
            'v': '5.52'
        }).json()

    server = response['response']['upload_url']

    # Подготавливаем файл для отправки и отправляем его
    file = requests.get(url, allow_redirects=True).content
    response = requests.post(server, files=[file,]).json()

    # Подтверждаем сохранение файла и получаем его данные в виде json
    result_json = requests.get('https://api.vk.com/method/photos.save',
                               params={
                                   'access_token': settings.VK_ACCESS_TOKEN,
                                   'album_id': response['aid'],
                                   'group_id': response['gid'],
                                   'server': response['server'],
                                   'photos_list': response['photos_list'],
                                   'caption': caption,
                                   'hash': response['hash'],
                                   'v': '5.52'
                               }).json()

    print(result_json)


@transaction.atomic
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for product in ShopProduct.objects.all():

            params_filter = ShopProductParams.objects.filter(
                product_id=product.id)

            if update_date_changed(params_filter, product):
                images = list(
                    ShopProductImages.objects.filter(product_id=product.id))
                filename = f'{images[0].id}.{images[0].ext}'
                url_base = 'http://yan-spb.tk/wa-data/protected'
                url = (
                    f'{url_base}/shop/products/0{product.id}/00'
                    f'/{product.id}/images/{filename}'
                )
                caption = f'{product.name}'
                post_photo(caption, url)
