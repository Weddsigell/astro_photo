import os
import requests
from environs import Env
from img_download import img_download
import argparse


def createParser():
    parser = argparse.ArgumentParser(description='Скачивает фото запуска ракет spacex')
    parser.add_argument(
        '--dirname',
        help=f'путь, куда скачивать фото, по умолчанию {env.str('IMAGES')}',
        default=env.str('IMAGES')
    )
    parser.add_argument(
        '--flight_id',
        help='id полета, иначе берет последний полет',
        default='latest'
    )
    return parser.parse_args()


def fetch_spacex_last_launch(dirname, flight_id='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{flight_id}'
    response = requests.get(url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']

    for url_number, url in enumerate(urls):
        path_file = os.path.join(dirname, f'spacex_{url_number}.jpg')
        img_download(url, path_file)


if __name__ =='__main__':
    env = Env()
    env.read_env()
    args = createParser()
    fetch_spacex_last_launch(args.dirname, args.flight_id)
