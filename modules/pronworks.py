#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Aug 20, 2023
# Links       : https://github.com/s0rkin/
# version ='1.1'
# ---------------------------------------------------------------------------

import os
import requests
import json
import time
import random

#load file .env config
from dotenv import load_dotenv
load_dotenv()

header = {
    "Accept": "application/json; charset=utf-8",
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST"),
    "referer": os.getenv("BOOBS_URL") + "/en/generate/image"
    }

proxies_socks = {
    "http": os.getenv("PROXY_HOST"),
    "https": os.getenv("PROXY_HOST"),
}

#girls hair for random
girls = [
  "Black hair",
  "Brown hair",
  "Dark brown hair",
  "Light brown hair",
  "Blonde hair",
  "Platinum blonde hair",
  "Golden blonde hair",
  "Strawberry blonde hair",
  "Red hair",
  "Auburn hair",
  "Copper hair",
  "Ginger hair",
  "Brunette hair",
  "Ash brown hair",
  "Chestnut hair",
  "Mahogany hair",
  "Gray hair",
  "Silver hair",
  "White hair"
]

#model it can be change, see on pornworks.com for free models.
models = ["nude_people", "real_porn_pony", "hardcore_fantasy"]

#main data for post
data = {
    "cfgScale": 7,
    "checkpoint": random.choice(models),
    "fast": False,
    "hr": False,
    "negativePrompt": "(vaginal sex:1.5), painting, vagina, sketches, lowers, monochrome, grayscale, skin spots, acnes, skin blemishes, age spot, (outdoor:1.2), fat, mole, g_deepnegative_v1_75t, (((poorly drawn hands))), (worst quality:2), (low quality:2), (normal quality:2), cat ears, elf ears, tail, wings, pointed ears, lowres, extra glans, extra fingers, fewer fingers, strange fingers, bad hand, jpeg, artifacts, signature, ugly, pregnant, vore, duplicate, morbid, mutilated, tranny, trans, trannsexual, hermaphrodite, extra hands, fused fingers, long neck, mutated hands, poorly drawn face, mutation, deformed, blurry, bad anatomy, bad proportions, malformed limbs, extra limbs, cloned face, disfigured, more than 2 nipples, missing arms, missing legs, extra arms, (extra legs), extra toes, missing fingers, deformed fingers, panties, panty, thong, red eyes, fake tits, christmas elf, elf cap, cap, hat, (((multiple sets of ears:1.3))), (bad-hands-5:1.2), nipples, focus on breast, cropped, scars, out of frame, dehydrated, gross proportions, too many fingers, asian appearance, japan appearance, scars on the body",
    "nsfw": True,
    "performance": "express", #express // quality
    "prompt": random.choice(girls) + ", 1girl, underboob, skin indentation, long hair, breasts, (large breasts:1.1), (beautiful face:1.2), (makeup, lipstick, blush, eyeliner:0.8), sweaty skin, perfect body, nude, high definition photo, ultra detailed skin, ultra detailed face, natural lighting, depth of field, canon r5, 8k uhd, (natural colors:1.2), random background place, large perky boobs, topless nude, light smile, realistic detailed eyes, ealistic detailed face, realistic detailed tan skin, nose freckles, full body, cute, ultra realistic, masterpiece, extremely sensual, perfect boobs, white, wet body, wet hair, perfect fingers and hands, amateur photograph, intricate details, perfect tits, shirt, pale skin, her hands on her tits, side view, flash photo, panties aside, (very slutty and sexy makeup, athletic, perfect eyelashes, blush, lipgloss, perfect face), sensual pose, wide shot, from below, photorealistic, ziprealism",
    "resources": [],
    "sharpness": 5,
    "ratio": "9x16",
    "size": "1024x1024", 
}

def set_boobs(num_retries = 15):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("BOOBS_API_URL") + "/text2image", headers=header, json=data, proxies=proxies_socks)
            print(r)
            print(r.status_code)
            print(r.text)
            t = json.loads(r.text)
            j = t["id"]
            return j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(10) #WAIT 60sec - DONT SPAM API!
                print("set_boobs attempts left: " + str(num_retries - attempt_no - 1))
                continue
            else:
                print("API ERROR! set_boobs " + str(num_retries) + " attempts expired!")
                break

get_id = set_boobs()

def get_boobs(num_retries = 90):
    if get_id:
        for attempt_no in range(num_retries):
            try:
                r = requests.get(os.getenv("BOOBS_API_GENERATOR_URL") + get_id +  "/state", headers=header, proxies=proxies_socks)
                print(r.text)
                t = json.loads(r.text)
                local_file_name = os.getenv("PATH_FOR_IMG") + get_id + ".png"
                img_url = t["results"]["image"]
                print(img_url)
                r_img = requests.get(img_url, stream=True, headers=header, proxies=proxies_socks)
                open(local_file_name, "wb").write(r_img.content)
                return local_file_name
            except:
                if attempt_no < (num_retries - 1):
                    time.sleep(15)
                    print("get_boobs attempts left: " + str(num_retries - attempt_no - 1))
                    continue
                else:
                    print("API ERROR! get_boobs " + str(num_retries) + " attempts expired!")
                    break
    else:
        return os.getenv("IMG_EXCEPT")

get_boobs_file = get_boobs()
