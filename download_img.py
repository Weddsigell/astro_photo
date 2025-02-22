import os
from pathlib import Path
from urllib import parse
import requests


def get_extension(img_url):
    img_path = parse.urlparse(img_url).path
    img_path = parse.unquote(img_path, encoding='utf-8', errors='replace')
    img_name = os.path.split(img_path)[1]
    return os.path.splitext(img_name)[1]


def download_img(img_url, path_file, payload=None):
    if payload is None:
        payload = {}

    response = requests.get(img_url, params=payload)
    response.raise_for_status()
    dirname = os.path.split(path_file)[0]
    Path(dirname).mkdir(parents=True, exist_ok=True)
    with open(path_file, 'wb') as file:
        file.write(response.content)
