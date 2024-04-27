#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Aug 20, 2023
# Links       : https://github.com/s0rkin/
# version ='1.0'
# ---------------------------------------------------------------------------

import os
import requests
import json
import time

#load file .env config
from dotenv import load_dotenv
load_dotenv()

header = {
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST"), 
    "Authorization": os.getenv("HEADER_AUTHORIZATION")
    }

post_info = {
  "messages": [
    {
        "role": "user", #role's (system, assistant, user)
        "content": "напиши уникальное,забавное,короткое поздравление для коллег в честь вечера пятницы"
    }
  ],
  "model": "gpt-3.5-turbo", #gpt-4
  "temperature": 1, #chaptgpt recomend 0.7-1.0
  "presence_penalty": 0,
  "top_p": 1, #chaptgpt recomend 0.7-1.0
  "frequency_penalty": 0,
  "stream": False
}

def get_text(num_retries = 15):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("GPT_URL"), headers=header, json=post_info)
            t = json.loads(r.text)
            j = t["choices"][0]["message"]["content"]
            return j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(60) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_text): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API (get_text) ERROR! " + str(num_retries) + " retries expired! Return default text")
                return "ChatGPT error! nothing will be send -_-"