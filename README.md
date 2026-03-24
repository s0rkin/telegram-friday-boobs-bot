# BOT "Friday boobs" for Telegram - 18+ only!

![Screenshot 1](https://github.com/s0rkin/telegram-friday-boobs-bot/assets/12657938/c74911ee-85fc-47f7-b726-c182fc378d9b)

## Описание

Телеграм-бот для автоматической публикации контента (18+). Публикует изображения по пятницам.

## Текущая версия

- 1.1
- telethon удалён
- telebot добавлен
- мелкие исправления в pron-модуле

## Конфигурация (.env)

```dotenv
PATH_FOR_IMG="/home/user/"
IMG_EXCEPT="/home/user/404.jpg"
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_STRING_SESSION=
CALENDAR_URL="https://api.sm.su/v1/calendar/business/"
GPT_URL=""
BOOBS_URL="https://www.pornworks.com"
BOOBS_API_URL="https://www.pornworks.com/api/v2/generate"
BOOBS_API_GENERATOR_URL="https://www.pornworks.com/api/v2/generations/"
TELEGRAM_GROUP=
TELEGRAM_USER="User"
HEADER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
HEADER_REQUEST="XMLHttpRequest"
```

### Обязательные поля

- `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_STRING_SESSION`
- `PATH_FOR_IMG` — путь к изображениям
- `IMG_EXCEPT` — резервное изображение (404.jpg)

### Опции

- `GPT_URL` — URL для GPT (рекомендуется gpt4free: https://github.com/xtekky/gpt4free/tree/main)
- `TELEGRAM_GROUP` — `-1234567890` (для отправки в группу)
- `TELEGRAM_USER` — имя пользователя для личных сообщений
- `HEADER_AUTHORIZATION` — авторизация для GPT (см. `gpt.py`)

## Как получить данные Telegram

1. Зарегистрировать приложение в Telegram и получить `API_ID` и `API_HASH`.

## Запуск

```bash
python3 main.py
```

## Поставить в cron (по пятницам в 18:25)

```cron
25 18 * * 5 /usr/bin/python3 /home/user/main.py >> /var/log/main_boobs_friday_bot.log 2>&1
```

## Полезные заметки

- `GPT_URL` — адрес ChatGPT/клон-сервиса.
- Контент 18+ — используйте ответственно.

## ⚠️ Важно

- Не публикуйте `.env` с реальными данными.

## 📄 Лицензия

MIT

## 🤝 Вклад в проект

Предложения по улучшению приветствуются. Открывайте issue или pull request.