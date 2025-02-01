import requests
from environs import Env
from img_download import img_download
import argparse


def createParser():
    parser = argparse.ArgumentParser(description='Скачивает последние фото Земли')
    parser.add_argument(
        '--nasa_api',
        help=f'api nasa, берется из env файла',
        default=env.str('NASA_API')
    )
    parser.add_argument(
        '--path_file',
        help=f'путь, куда скачивать фото, по умолчанию {env.str('IMAGES')}',
        default=env.str('IMAGES')
    )
    parser.add_argument(
        'count',
        help='кол-во фото',
        type=int
    )
    return parser.parse_args()


def get_nasa_epic(nasa_api, path_file, count):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_api,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    datas = response.json()
    for img_number, img in enumerate(datas):
        img_name = img['image']
        date = img['date'].split(' ')[0].split('-')
        img_url = ('https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png?api_key={}'
                   .format(date[0], date[1],date[2],img_name,nasa_api))
        print(img_url)
        img_download(img_url, path_file, f'epic_{img_number}.png')

        if count <= (img_number + 1):
            break


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = createParser()
    get_nasa_epic(args.nasa_api, args.path_file, args.count)
