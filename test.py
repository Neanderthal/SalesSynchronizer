# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import json
from time import sleep

import requests

#https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=5.52
def main():
    group_id = '175030782'
    album_id = '258677915'
    access_token = '3dafe3da022feb6f1b66b195f35840576cb830a47ba3005730937e242bd85d11fa99d9a2381cf56189d0d'
    filename = 's1200.jpeg'
    caption = 'Енот'

    #Получаем адрес сервера для загрузки фотографии
    response = requests.get('https://api.vk.com/method/photos.getUploadServer', params= {
        'access_token': access_token,
        'album_id': album_id,
        'group_id': group_id,
        'v': '5.52'
    }).json()

    server = response['response']['upload_url']

    #Подготавливаем файл для отправки и отправляем его
    file = {'file1': open('/data/PycharmProjects/test_test/6.jpg', 'rb')}
    response = requests.post(server, files=file).json()

    #Подтверждаем сохранение файла и получаем его данные в виде json
    result_json = requests.get('https://api.vk.com/method/photos.save', params= {
        'access_token': access_token,
        'album_id': response['aid'],
        'group_id': response['gid'],
        'server': response['server'],
        'photos_list': response['photos_list'],
        'caption': 'Просто енот',
        'hash': response['hash'],
        'v': '5.52'
    }).json()

    print(result_json)
    sleep(1)

if __name__ == '__main__':
    main()