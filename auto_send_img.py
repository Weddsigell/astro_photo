import argparse
import time
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
        default='./images'
    )
    parser.add_argument(
        '--time',
        help=f'промежуток времени в часах, для циклической публикации, по умолчанию 4 часа',
        type=int,
        default=4
    )
    return parser.parse_args()


def sending_cycle(tg_token, tg_chat_id, dirname, delay):
    while True:
        photos = select_photo(dirname)

        for photo in photos:
            send_photo(tg_token, tg_chat_id, photo)
            time.sleep(delay * 60 * 60) #часы * минуты * секунды = секунды


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = create_parser()
    sending_cycle(args.tg_token, args.tg_chat_id, args.dirname, args.time)
