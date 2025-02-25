import argparse
import time
from pathlib import Path
import telegram
from environs import Env
from send_img import select_photo, send_photo


def create_parser():
    parser = argparse.ArgumentParser(description='Автоматически публикует все фото из директории в телеграмм канал')
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
        help=f'путь, куда скачивать фото',
        default=Path.cwd() / 'images',
        type=Path
    )
    parser.add_argument(
        '--time',
        help=f'промежуток времени в часах, для циклической публикации, по умолчанию 4 часа',
        type=int,
        default=4
    )
    return parser.parse_args()

def wait_response(tg_token, tg_chat_id, photo):
    is_connect = False
    while not is_connect:
        try:
            send_photo(tg_token, tg_chat_id, photo)
            is_connect = True
        except telegram.error.TelegramError:
            time.sleep(10)

def sending_cycle(tg_token, tg_chat_id, dirname, delay):
    while True:
        photos = select_photo(dirname)

        for photo in photos:
            try:
                send_photo(tg_token, tg_chat_id, photo)
            except telegram.error.TelegramError:
                wait_response(tg_token, tg_chat_id, photo)

            time.sleep(delay * 60 * 60) #часы * минуты * секунды = секунды


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = create_parser()
    sending_cycle(args.tg_token, args.tg_chat_id, args.dirname, args.time)
