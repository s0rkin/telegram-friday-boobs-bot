# BOT "Friday boobs" for telegram, on your profile!
![Screenshot_1](https://github-production-user-asset-6210df.s3.amazonaws.com/12657938/321216868-bb640698-2a97-4416-8851-cdb63a1bdd91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240410%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240410T112826Z&X-Amz-Expires=300&X-Amz-Signature=7123d1f6dd361b1364805681a851dee991c46dadfb83d7e0abff9ab11b6c9a73&X-Amz-SignedHeaders=host&actor_id=12657938&key_id=0&repo_id=784685689)
<br>
<p>CONFIG in <code>.env</code>:
<code>
    PATH_FOR_IMG="/home/user/"
    IMG_EXCEPT=""
    TELEGRAM_API_ID=
    TELEGRAM_API_HASH=
    TELEGRAM_STRING_SESSION=
    CALENDAR_URL="https://api.sm.su/v1/calendar/business/"
    GPT_URL=""
    BOOBS_URL="https://www.pornworks.ai"
    BOOBS_API_URL="https://www.pornworks.ai/api/v2/generate"
    BOOBS_API_GENERATOR_URL="https://www.pornworks.ai/api/v2/generations/"
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
GPT_URL - chatgpt url , google it! can be free! =)</text>
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