import argparse
import os
import random
import time
from environs import Env
import telegram


def createParser():
    parser = argparse.ArgumentParser(description='Скачивает последние фото Земли')
    parser.add_argument(
        '--tg_token',
        help=f'берется из env файла',
        default=env.str('TG_TOKEN')
    )
    parser.add_argument(
        '--tg_chat_id',
        help=f'берется из env файла',
        default=env.str('TG_ID_CHANEL')
    )
    parser.add_argument(
        '--dirname',
        help=f'каталог с фото, берется из env файла',
        default = env.str('IMAGES')
    )
    parser.add_argument(
        'time',
        help=f'промежуток времени в часах, для циклической публикации',
        type=int,
        default=4
    )
    return parser.parse_args()


def send_photo(tg_token, tg_chat_id, path_file):
    bot = telegram.Bot(tg_token)
    bot.send_document(chat_id=tg_chat_id, document=open(path_file, 'rb'))


def photo_selection(dirname):
    photos = []
    ext = ('.png', '.jpg')
    for tuple in os.walk(dirname):
        for filename in tuple[2]:
            file = os.path.join(tuple[0], filename)
            if file.endswith(ext):
                photos.append(file)
            else:
                continue

    random.shuffle(photos)
    return photos


def sending_cycle(tg_token, tg_chat_id, dirname, delay):
    while True:
        photos = photo_selection(dirname)

        for photo in photos:
            send_photo(tg_token, tg_chat_id, photo)
            time.sleep(delay)




if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = createParser()
    sending_cycle(args.tg_token, args.tg_chat_id, args.dirname, args.time)