# Космический Телеграм
Набор скриптов, позволяющий скачивать фото и публиковать их в телеграмм канал

### Как установить
Python3 должен быть уже установлен. 

Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом со скриптами и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `TG_TOKEN` — токен телеграмм бота, инструкция по ссылке https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html
- `TG_ID_CHANEL` — chat_id канала — это ссылка на него, например: @dvmn_flood

### Как использовать
Имеется 5 скриптов, для получения подробной информации по каждому скрипту
* `python get_apods_photo -h` - скачивает фото дня с сайта nasa
* `python get_epic_photo -h` - скачивает последние фото нашей планеты
* `python get_spacex_launch_photo -h` -  скачивает фото запуска ракет spacex
* `python send_img -h` - публикует фото в телеграмм канал (для использования нужно сделать вашего бота администратором канала)
* `python auto_send_img -h` - автоматически публикует фото в телеграмм канал (для использования нужно сделать вашего бота администратором канала)


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
 
