#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Aug 20, 2023
# Links       : https://github.com/s0rkin/
# version ='1.0'
# ---------------------------------------------------------------------------

import os
import datetime

from modules import gpt, pronworks, workday
from telethon.sync import TelegramClient, types
from telethon.sessions import StringSession
from dotenv import load_dotenv

#load file .env config
load_dotenv()

today = datetime.datetime.today()

print("---------------------------------------------------------------------------")
print(today)

text_from = "<code>Сгенерировано нейросетью PornWorks.ai + ChatGPT! by s0rry</code>"

#TELEGRAM CLIENT
try:
    client = TelegramClient(StringSession(os.environ.get("TELEGRAM_STRING_SESSION")), os.environ.get("TELEGRAM_API_ID"), os.environ.get("TELEGRAM_API_HASH"))
    client.start()
except Exception as e:
    print(f"Exception while starting the client - {e}")
else:
    print("Client started")

#main function for send message to telegram chat
async def main():
    try:
        uploaded = await client.upload_file(pronworks.get_boobs_file)
        #client.send_message need int for group only!
        # os.getenv("TELEGRAM_USER") // int(os.getenv("TELEGRAM_GROUP"))
        ret_value = await client.send_file(int(os.getenv("TELEGRAM_GROUP")), types.InputMediaUploadedPhoto(uploaded, spoiler=True))
        ret_value = await client.send_message(int(os.getenv("TELEGRAM_GROUP")), workday.work_day + "\n" + "\n" + gpt.gpt_text + "\n" + "\n" + text_from, parse_mode="html")
    except Exception as e:
        print(f"Exception while sending the message - {e}")
    else:
        print(f"Message sent. Return Value {ret_value}")

with client:
    client.loop.run_until_complete(main())