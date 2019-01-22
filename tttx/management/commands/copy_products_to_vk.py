# -*- coding: utf-8 -*-
import requests
from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction
import vk

from tttx.models import ShopProduct, ShopProductImages


@transaction.atomic
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for product in ShopProduct.objects.all():
            images = list(ShopProductImages.objects.filter(product_id=product.id))
            filename = f'{images[0].id}.{images[0].ext}'
            url_base = 'http://yan-spb.tk/wa-data/protected'
            url = (
                f'{url_base}/shop/products/0{product.id}/00'
                f'/{product.id}/images/{filename}'
            )
            caption = f'{product.name}'
            self.post_photo(caption, url)

        pass

    def post_photo(self, caption, url):
        session = vk.AuthSession(app_id='6015721',
                                 access_token=settings.VK_ACCESS_TOKEN)
        api = vk.API(session, v='5.73')

        r = requests.get(url, allow_redirects=True)

        # Получаем адрес сервера для загрузки картинки
        upload_url = api.photos.getUploadServer(
            album_id=settings.VK_ALBUM_ID,
            group_id=settings.VK_GROUP_ID,
            access_token=settings.VK_ACCESS_TOKEN)['upload_url']
        # Формируем данные параметров для сохранения картинки на сервере
        request = requests.post(
            upload_url, files={'photo': r.content})
        params = {'server': request.json()['server'],
                  'photo': request.json()['photo'],
                  'hash': request.json()['hash'],
                  'group_id': settings.VK_GROUP_ID,
                  'album_id': settings.VK_ALBUM_ID}
        # Сохраняем картинку на сервере и получаем её идентификатор
        photo_id = api.photos.save(**params)[0]['id']
        # Формируем параметры для размещения картинки в группе и публикуем её
        params = {'attachments': photo_id,
                  'message': caption,
                  'owner_id': '-' + settings.VK_GROUP_ID,
                  'from_group': '1'}
        api.wall.post(**params)
