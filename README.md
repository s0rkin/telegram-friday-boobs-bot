# BOT "Friday boobs" for telegram, on your profile! 18+ only!
![Screenshot_1](https://github.com/s0rkin/telegram-friday-boobs-bot/assets/12657938/c74911ee-85fc-47f7-b726-c182fc378d9b)
<br>
<p>Current ver. 1.1
<code>
*add python 3.8
*delete telethon
*add telebot
*small fix'es pron
</code>
</p>
<p>CONFIG in <code>.env</code>:
<code>
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
</code>
</p>
<p>
u need to add some base URL -
</p>
<p>
GPT_URL - FOR GPT good idea - use Gpt4free https://github.com/xtekky/gpt4free/tree/main</text>
</p>
<p>then u need add - 
</p>
<p>
TELEGRAM_GROUP - EXAMPLE -> TELEGRAM_GROUP=-1234567890  // see more on <code>main.py</code> client send message!
</p>
<p>
TELEGRAM_USER - if need, EXAMPLE -> TELEGRAM_USER="user"
</p>
<p>
HEADER_AUTHORIZATION - this is authorization for GPT! - see more in <code>gpt.py</code> (u need add url and header's). google it!
</p>
<p>
add TELEGRAM config's google how to catch. or use <code>get_string_session.py</code>
</p>
<p>
TELEGRAM_API_ID=
</p>
<p>
TELEGRAM_API_HASH=
</p>
<p>
TELEGRAM_STRING_SESSION=
</p>
<p>ADD TO CRON, EXAMPLE:
<code>25 18 * * 5 /usr/bin/python3 /home/user/main.py >> /var/log/main_boobs_friday_bot.log</code>
</p>
