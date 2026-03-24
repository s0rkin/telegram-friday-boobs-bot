# BOT "Friday boobs" for Telegram - 18+ only!

![Screenshot 1](https://github.com/s0rkin/telegram-friday-boobs-bot/assets/12657938/c74911ee-85fc-47f7-b726-c182fc378d9b)

## Description

A Telegram bot for automatic publishing of adult content (18+). Posts images on Fridays.

## Current version

- 1.1
- telethon removed
- telebot added
- minor fixes in the pron module

## Configuration (.env)

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

### Required fields

- `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_STRING_SESSION`
- `PATH_FOR_IMG` — path to images
- `IMG_EXCEPT` — fallback image (404.jpg)

### Optional fields

- `GPT_URL` — URL for GPT (recommended: gpt4free: https://github.com/xtekky/gpt4free/tree/main)
- `TELEGRAM_GROUP` — `-1234567890` (for group messages)
- `TELEGRAM_USER` — username for direct messages
- `HEADER_AUTHORIZATION` — authorization for GPT (see `gpt.py`)

## How to get Telegram credentials

1. Register an app in Telegram and get `API_ID` and `API_HASH`.
2. Generate `STRING_SESSION` using `get_string_session.py`.

## Run

```bash
python3 main.py
```

## Cron schedule (every Friday at 18:25)

```cron
25 18 * * 5 /usr/bin/python3 /home/user/main.py >> /var/log/main_boobs_friday_bot.log 2>&1
```

## Notes

- `GPT_URL` is the ChatGPT/clone service URL.
- This is 18+ content, use responsibly.

## ⚠️ Important

- Do not publish `.env` with real credentials.

## 📄 License

MIT

## 🤝 Contribution

Contributions are welcome. Open an issue or pull request.