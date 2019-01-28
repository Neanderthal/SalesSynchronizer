# -*- coding: utf-8 -*-
import requests
import vk
from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

group_id = '175030782'
album_id = '258677915'
photo_id = '456239019' #Енот
access_token = '1fc9499c366cd96e511fe8b76f8a1cce092fc03bba19e03cc57c8dccf8b25fa95b4d7c2cd0af2ccf3dbf2'
group_access_token = 'a81677a7406d38026fb4748c6c41078e6578969d3aa622b60221aa9525fbc728d95169bb61f61a71baa7b'
webasyst_token = '89e6b8ede056a40eadd540228134b2a3'

from tttx.models import ShopProduct, ShopProductImages


@transaction.atomic
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        id = "456239019"

        # https: // vk.com / photo - 140432051_456244392/
        # https: // vk.com / album - 140432051_242677535

        # https: // vk.com / album - 117453470_229654516
        owner_id = "-175030782"

        response = requests.get('https://api.vk.com/method/photos.get', params={
            'access_token': access_token,
            'owner_id': '-140432051',
            'album_id': '242677535',
            'rev': 1,
            'offset': 1,
            'count': 1,
            'v': '5.92'
        }).json()

        print(response)
        print(response['response']['items'][0]['sizes'][9]['url'])

        # for product in ShopProduct.objects.all():
        #     images = list(ShopProductImages.objects.filter(product_id=product.id))
        #     filename = f'{images[0].id}.{images[0].ext}'
        #     url_base = 'http://yan-spb.tk/wa-data/protected'
        #     url = (
        #         f'{url_base}/shop/products/0{product.id}/00'
        #         f'/{product.id}/images/{filename}'
        #     )
        #     caption = f'{product.name}'
        #     self.post_photo(caption, url)