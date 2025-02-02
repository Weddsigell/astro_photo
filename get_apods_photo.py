import os
import requests
from environs import Env
from img_download import get_extension, img_download
import argparse


def createParser():
    parser = argparse.ArgumentParser(description='Скачивает лучшие фото')
    parser.add_argument(
        '--nasa_api',
        help=f'api nasa, берется из env файла',
        default=env.str('NASA_API')
    )
    parser.add_argument(
        'count',
        help='кол-во фото'
    )
    parser.add_argument(
        '--dirname',
        help=f'путь, куда скачивать фото, по умолчанию {env.str('IMAGES')}',
        default=env.str('IMAGES')
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
    urls = []
    for apod in datas:
        urls.append(apod['url'])

    for url_number, url in enumerate(urls):
        ext = get_extension(url)
        path_file = os.path.join(dirname, f'nasa_apod_{url_number}{ext}')
        img_download(url, path_file)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = createParser()
    get_nasa_apods(args.nasa_api, args.count, args.dirname)
