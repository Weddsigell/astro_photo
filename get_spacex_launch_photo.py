import requests
from environs import Env
from img_download import img_download
import argparse


def createParser():
    parser = argparse.ArgumentParser(description='Скачивает фото запуска ракет spacex')
    parser.add_argument(
        '--path_file',
        help=f'путь, куда скачивать фото, по умолчанию {env.str('IMAGES')}',
        default=env.str('IMAGES')
    )
    parser.add_argument(
        '--flight_id',
        help='id полета, иначе берет последний полет',
        default='latest'
    )
    return parser.parse_args()


def fetch_spacex_last_launch(path_file, flight_id='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{flight_id}'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']

    for link_number, link in enumerate(links):
        img_download(link, path_file, f'spacex_{link_number}.jpg')


if __name__ =='__main__':
    env = Env()
    env.read_env()
    args = createParser()
    fetch_spacex_last_launch(args.path_file, args.flight_id)
