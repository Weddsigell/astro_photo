from environs import Env
import telegram


def main():
    tg_tоken = env.str('TG_TOKEN')
    bot = telegram.Bot(tg_tоken)
    bot.send_message(text='Добро пожаловать в канал с астро фото', chat_id=env.str('TG_ID_CHANEL'))


if __name__ == '__main__':
    env = Env()
    env.read_env()
    main()
