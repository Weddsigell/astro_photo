import argparse
import os
import random
from pathlib import Path
from environs import Env
import telegram


def create_parser():
    parser = argparse.ArgumentParser(description='Публикует фото в телеграмм канал')
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
        '--path_file',
        help=f'фото которое нужно опубликовать, по умолчанию случайное фото из директории ./images',
        default='./images'
    )
    return parser.parse_args()


def send_photo(tg_token, tg_chat_id, path_file):
    bot = telegram.Bot(tg_token)
    with open(path_file, 'rb') as file:
        bot.send_document(chat_id=tg_chat_id, document=file)



def select_photo(dirname):
    ext = ('.png', '.jpg')
    photos = [os.path.join(tuple[0], filename) for tuple in Path(dirname).walk() for filename in tuple[2] if filename.endswith(ext)]
    random.shuffle(photos)
    return photos


if __name__ == '__main__':
    env = Env()
    env.read_env()
    args = create_parser()
    if args.path_file == './images':
        args.path_file = select_photo(args.path_file)[0]
    send_photo(args.tg_token, args.tg_chat_id, args.path_file)
