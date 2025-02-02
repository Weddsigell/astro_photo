from environs import Env
import telegram


def main():
    tg_tоken = env.str('TG_TOKEN')
    bot = telegram.Bot(tg_tоken)
    bot.send_message(text='Добро пожаловать в канал с астро фото', chat_id=env.str('TG_ID_CHANEL'))
    bot.send_document(chat_id=env.str('TG_ID_CHANEL'), document=open('./images/epic_0.png', 'rb'))


if __name__ == '__main__':
    env = Env()
    env.read_env()
    main()
