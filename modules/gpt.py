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
    }

post_info = {
  "model": 'gpt-4o-mini', #gpt-4
  "temperature": 0.9, #chaptgpt recomend 0.7-1.0
  "stream": False, 
  "messages": [
    {
        "role": "user", #role's (system, assistant, user)
        "content": "напиши уникальное,забавное,короткое поздравление для коллег в честь вечера пятницы"
    }
  ]
}

def get_text(num_retries = 15):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("GPT_URL"), headers=header, json=post_info)
            t = json.loads(r.text)
            j = t["choices"][0]["message"]["content"]
            #Очередной костыль для GPT, когда он игнорирует флаг stream: False
            if "data:" in j:
                # Разделяем текст на строки
                lines = j.strip().split("\n\n")

                result = ""
                for line in lines:
                    try:
                        # Убираем префикс "data: "
                        json_str = line.replace("data: ", "")

                        # Пропускаем пустые строки
                        if not json_str.strip():
                            continue
                        
                        obj = json.loads(json_str)

                        if isinstance(obj, dict) and "content" in obj and obj["content"]:
                            result += obj["content"]
                    except json.JSONDecodeError as e:
                        print(f"Ошибка декодирования JSON: {e}. Строка: {line}")
                        continue
                return result
            else:
                return j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(60) #wait 30sec for api response if have error. DONT SPAM!
                print("CURRENT RETRY (get_text): " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API (get_text) ERROR! " + str(num_retries) + " retries expired! Return default text")
                return "ChatGPT error! nothing will be send -_-"
