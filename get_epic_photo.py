from datetime import datetime
from pathlib import Path
import requests
from environs import Env
from download_img import download_img
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Скачивает последние фото Земли')
    parser.add_argument(
        '--nasa_api',
        help=f'ключ api от nasa',
        default='DEMO_KEY'
    )
    parser.add_argument(
        '--dirname',
        help=f'путь, куда скачивать фото',
        default=Path.cwd() / 'images',
        type=Path
    )
    parser.add_argument(
        '--count',
        help='кол-во фото',
        type=int,
        default=1
    )
    return parser.parse_args()


def get_nasa_epic(nasa_api, dirname, count):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_api,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    datas = response.json()
    for img_number, img in enumerate(datas):
        img_name = img['image']
        date = datetime.fromisoformat(img['date']).strftime('%Y/%m/%d')
        payload = {'api_key': nasa_api}
        img_url = ('https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
                   .format(date, img_name))
        path_file = Path(dirname) / f'epic_{img_number}.png'
        download_img(img_url, path_file, payload)

        if count <= (img_number + 1):
            break


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = create_parser()
    get_nasa_epic(args.nasa_api, args.dirname, args.count)
