# -*- coding: utf-8 -*-
import io
from datetime import datetime
from dateutil import parser
import requests
import os
from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

from tttx.models import ShopProduct, ShopProductImages, ShopProductParams


def update_date_changed(product):
    params_filter = ShopProductParams.objects.filter(
        product_id=product.id, name='saved_date')
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
        if not parser.parse(product_param.value) == saved_date:
            product_param.value = saved_date
            product_param.save()
            date_changed = True

    return date_changed


def post_photo(caption, download_url, filename):
    album_id = settings.VK_ALBUM_ID,
    group_id = settings.VK_GROUP_ID,

    file = requests.get(download_url, allow_redirects=True).content

    # Получаем адрес сервера для загрузки фотографии
    upload_url = get_upload_url(album_id, group_id)

    with open(filename, "wb") as f:
        f.write(file)

    # Подготавливаем файл для отправки и отправляем его
    stream = open(filename, "rb")
    print((f'size: {os.path.getsize(filename)}'
           f'caption {caption} filename {filename} upload  {download_url}'))
    files = {'file1': stream}

    response = requests.post(upload_url, files=files).json()

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
                                   'v': '5.92'
                               }).json()

    print(result_json)


def get_upload_url(album_id, group_id):
    response = requests.get(
        'https://api.vk.com/method/photos.getUploadServer', params={
            'access_token': settings.VK_ACCESS_TOKEN,
            'album_id': album_id,
            'group_id': group_id,
            'v': '5.52'
        }).json()
    server = response['response']['upload_url']
    return server


@transaction.atomic
class Command(BaseCommand):
    transaction.atomic()

    def handle(self, *args, **kwargs):
        for product in ShopProduct.objects.all():
            if update_date_changed(product):
                images = list(
                    ShopProductImages.objects.filter(product_id=product.id))
                if images:
                    filename, url = self.get_image_url(product)
                    caption = f'{product.name}'
                    post_photo(caption, url, filename)

    def get_image_url(self, product):
        content = requests.get(
            f"http://yan-spb.tk/api.php/shop.product.images.getInfo",
            params={'id': product.image_id,
                    'access_token': settings.WEBASSYST_ACCESS_TOKEN
                    }).json()
        return content['original_filename'], content['url_big']
