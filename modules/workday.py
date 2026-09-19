#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Aug 20, 2023
# Links       : https://github.com/s0rkin/
# version ='1.2'
# ---------------------------------------------------------------------------

import os
import requests
import json
import time
from datetime import datetime

#load file .env config
from dotenv import load_dotenv
load_dotenv()

now = datetime.now()

header = {
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST")
    }

param = {
    "day": now.strftime("%Y-%m-%d")
}

#function get_day for working from work calendar
def get_day(num_retries = 10):
    for attempt_no in range(num_retries):
        try:
            r = requests.get(os.getenv("CALENDAR_URL"), headers = header, params = param)
            t = json.loads(r.text)
            #return full string for telegram "text" + get_day()
            if t["work"] == "1": #work day
                return "Рабочий день заканчивается! 😎😎😎"
            elif t["work"] == "0" and (t["zag"] == "Календарный выходной день" or t["zag"] == "Перенесенный день"): #not work day typical
                return "Сегодня нерабочий день! 😎😎😎"
            elif t["work"] == "0": #not work day holiday
                return "Сегодня праздничный нерабочий день! "
            else:
                return "Сегодня ХЗ рабочий или нет день! 😎😎😎"
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(30) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_day): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API (get_day) ERROR! 10 retries expired!")
                return "Рабочий день заканчивается! 😎😎😎 Сегодня ХЗ какой день."
