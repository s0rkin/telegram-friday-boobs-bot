#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Aug 20, 2023
# Links       : https://github.com/s0rkin/
# version ='1.1'
# ---------------------------------------------------------------------------

import os
import datetime
import telebot

from modules import gpt, workday, pronworks

from dotenv import load_dotenv
#load file .env config
load_dotenv()

today = datetime.datetime.now()

print("---------------------------------------------------------------------------")
print(today)

text_from = "<code>Сгенерировано нейросетью PornWorks.ai + ChatGPT! by s0rry</code>"

#crutch to disable the delay when sending img + message
boobs = pronworks.get_boobs_file
work = workday.get_day()
get_gpt = gpt.get_text()

# bot
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

# main function
def main():
    try:
        # uploaded photo
        uploaded = open(boobs, "rb")

        ret_value = bot.send_photo(
                int(os.getenv("TELEGRAM_GROUP")),
                uploaded,
                caption=work + "\n\n" + get_gpt + "\n" + "\n" + text_from,
                parse_mode="html",
                has_spoiler=True
            )
    except Exception as e:
        print(f"Exception while sending the message - {e}")
    else:
        print(f"Message sent. Return Value {ret_value}")

#start main
if __name__ == "__main__":
    main()