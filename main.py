import os
from datetime import datetime
import requests
from pathlib import Path
from environs import Env
from urllib import parse


env = Env()
env.read_env()


def download_img(img_url, path_file):
    response = requests.get(img_url)
    response.raise_for_status()
    Path(env.str("IMAGES")).mkdir(parents=True, exist_ok=True)
    with open(path_file, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(flight_id, path_file):
    url = f'https://api.spacexdata.com/v5/launches/{flight_id}'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']

    for link_number, link in enumerate(links):
        download_img(link, f'{path_file}/spacex_{link_number}.jpg')


def get_extension(img_url):
    img_path = parse.urlparse(img_url).path
    img_path = parse.unquote(img_path, encoding='utf-8', errors='replace')
    img_name = os.path.split(img_path)[1]
    return os.path.splitext(img_name)[1]


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
        download_img(link, f'{path_file}/nasa_apod_{link_number}{ext}')


def get_nasa_epic(nasa_api, path_file):
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
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{img_name}.png?api_key={env.str('NASA_API')}'
        download_img(img_url, f'{path_file}/epic_{img_number}.png')


def main():
    # fetch_spacex_last_launch('5eb87d47ffd86e000604b38a', env.str("IMAGES"))
    # get_nasa_apods(
    #     env.str('NASA_API'),
    #     '10',
    #     env.str("IMAGES")
    # )

    get_nasa_epic(
        env.str('NASA_API'),
        env.str("IMAGES")
    )

if __name__ =='__main__':
    main()
