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
        '--path_file',
        help=f'путь, куда скачивать фото, по умолчанию {env.str('IMAGES')}',
        default=env.str('IMAGES')
    )
    return parser.parse_args()


def get_nasa_apods(nasa_api, count, path_file):
    params = {
        'api_key': nasa_api,
        'count': count,
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    datas = response.json()
    links = []
    for apod in datas:
        links.append(apod['url'])

    for link_number, link in enumerate(links):
        ext = get_extension(link)
        img_download(
            link,
            path_file,
            f'nasa_apod_{link_number}{ext}'
        )


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = createParser()
    get_nasa_apods(args.nasa_api, args.count, args.path_file)
