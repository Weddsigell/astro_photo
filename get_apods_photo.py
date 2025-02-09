import os
import requests
from environs import Env
from download_img import get_extension, download_img
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Скачивает лучшие фото')
    parser.add_argument(
        '--nasa_api',
        help=f'ключ api от nasa',
        default='DEMO_KEY'
    )
    parser.add_argument(
        '--count',
        help='кол-во фото',
        default=1,
        type=int
    )
    parser.add_argument(
        '--dirname',
        help=f'путь, куда скачивать фото',
        default='./images'
    )
    return parser.parse_args()


def get_nasa_apods(nasa_api, count, dirname):
    params = {
        'api_key': nasa_api,
        'count': count,
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    datas = response.json()
    urls = [apod['url'] for apod in datas if apod['media_type'] == 'image']

    for url_number, url in enumerate(urls):
        ext = get_extension(url)
        path_file = os.path.join(dirname, f'nasa_apod_{url_number}{ext}')
        download_img(url, path_file)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = create_parser()
    get_nasa_apods(args.nasa_api, args.count, args.dirname)
