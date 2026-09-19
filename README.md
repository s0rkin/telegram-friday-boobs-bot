# BOT "Friday boobs" for Telegram - 18+ only!

![Screenshot 1](https://github.com/s0rkin/telegram-friday-boobs-bot/assets/12657938/c74911ee-85fc-47f7-b726-c182fc378d9b)

## Description

A Telegram bot for automatic publishing of adult content (18+). Posts images on Fridays.

## Current version

- 1.2
- telethon removed
- telebot added
- minor fixes in the pron module
- PornWorks requests now run through the free CloakBrowser Chromium 146 build.
- Added a persistent browser profile, proxy support, and Cloudflare challenge detection.
- Added Xvfb-based server startup without a permanently running browser or VNC session.
- API errors and PornWorks generation limits now return the configured fallback image without unnecessary retries.
- Updated and consolidated Python dependencies; removed obsolete Playwright browser files and duplicate packages.

## Configuration (.env)

```dotenv
PATH_FOR_IMG="/home/user/"
IMG_EXCEPT="/home/user/404.jpg"
TELEGRAM_TOKEN=""
CALENDAR_URL="https://api.sm.su/v1/calendar/business/"
GPT_URL=""
BOOBS_URL="https://www.pornworks.com"
BOOBS_API_URL="https://www.pornworks.com/api/v2/generate"
BOOBS_API_GENERATOR_URL="https://www.pornworks.com/api/v2/generations/"
TELEGRAM_GROUP=
HEADER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
HEADER_REQUEST="XMLHttpRequest"
PROXY_HOST="http://host:port"
BOOBS_BROWSER_HEADLESS="false"
BOOBS_BROWSER_TIMEOUT_MS="90000"
```

### Required fields

- `TELEGRAM_TOKEN` — token issued by BotFather
- `TELEGRAM_GROUP` — target chat ID, for example `-1234567890`
- `PATH_FOR_IMG` — path to images
- `IMG_EXCEPT` — fallback image (404.jpg)

### Optional fields

- `GPT_URL` — URL for GPT (recommended: gpt4free: https://github.com/xtekky/gpt4free/tree/main)
- `HEADER_AUTHORIZATION` — authorization for GPT (see `gpt.py`)

## How to configure Telegram

1. Create a bot with BotFather and copy its token to `TELEGRAM_TOKEN`.
2. Add the bot to the target chat and put its numeric ID in `TELEGRAM_GROUP`.

## Run

```bash
sudo apt-get install xvfb
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
xvfb-run -a -s '-screen 0 1280x800x24' .venv/bin/python main.py
```

The CloakBrowser profile and browser binary are stored inside the project in
`.cloakbrowser-profile` and `.cloakbrowser-cache`. The free legacy Chromium 146
build is downloaded automatically on first run; no license key is required.

## Cron schedule (every Friday at 18:25)

```cron
25 18 * * 5 cd /home/user/boobs && xvfb-run -a -s '-screen 0 1280x800x24' .venv/bin/python main.py >> /var/log/main_boobs_friday_bot.log 2>&1
```

## Project requirements

- Linux with Python 3.10 or newer and the `venv` module.
- Xvfb, required to run Chromium in headful mode on a server without a display.
- CloakBrowser Chromium, downloaded automatically on the first run.
- A writable directory configured by `PATH_FOR_IMG` and an existing fallback image configured by `IMG_EXCEPT`.
- Network access to PornWorks, Telegram, the calendar API, and the configured GPT endpoint.
- A proxy supporting the URL configured by `PROXY_HOST`, when proxying is enabled.

Only direct Python dependencies are listed in `requirements.txt`; pip installs
their transitive dependencies automatically inside `.venv`.

CloakBrowser uses a source-patched Chromium build and a persistent profile to
keep the browser fingerprint consistent between scheduled runs. The free build
is sufficient for the bot's single browser session.

PornWorks may respond with `SIGNUP_FOR_INCREASE_LIMIT` after Cloudflare has
already been passed. This is the site's free-generation limit, not a browser or
proxy error; generation then requires a PornWorks account or a renewed limit.


## Notes

- `GPT_URL` is the ChatGPT/clone service URL.
- This is 18+ content, use responsibly.

## ⚠️ Important

- Do not publish `.env` with real credentials.

## 📄 License

MIT

## 🤝 Contribution

Contributions are welcome. Open an issue or pull request.
