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
import random

#load file .env config
from dotenv import load_dotenv
load_dotenv()

header = {
    "Accept": "application/json; charset=utf-8",
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": os.getenv("HEADER_AGENT"),
    "X-Requested-With": os.getenv("HEADER_REQUEST"),
    "referer": os.getenv("BOOBS_URL") + "/ru/generate/image"
    }

#girls hair for random
girls = ["Black hair", "Brown hair", "Blonde hair", "Red hair", "Auburn hair", "Brunette hair", "Gray hair", "White hair", "Platinum hair", "Silver hair", "Golden hair", "Copper hair", "Mahogany hair", "Caramel hair", "Honey hair", "Ash hair", "Burgundy hair", "Violet hair", "Blue hair", "Green hair", "Pink hair", "Rainbow hair", "Ombre hair", "Balayage hair", "Lowlights hair"]
#model it can be change, see on pornworks.com ! see SIZE for models.
models = ["photon", "nude_people", "real_porn_pony"] #"hardcore_fantasy"

#main data for post
data = {
    "cfgScale": 10,
    "checkpoint": random.choice(models), #random models :)
    "denoisingStrength": 1,
    "fast": False,
    "hr": False,
    "inpaintMode": "checkpoint",
    #DISABLED PROMT! - dont change if u dont want porn photo and etc.
    "negativePrompt": "(vaginal sex:1.5), painting, vagina, sketches, lowers, monochrome, grayscale, skin spots, acnes, skin blemishes, age spot, (outdoor:1.2), fat, mole, g_deepnegative_v1_75t, (((poorly drawn hands))), (worst quality:2), (low quality:2), (normal quality:2), cat ears, elf ears, tail, wings, pointed ears, lowres, normal quality, acnes, age spot, extra glans, extra fingers, fewer fingers, strange fingers, bad hand, jpeg, artifacts, signature, ugly, pregnant, vore, duplicate, morbid, mutilated, tranny, trans, trannsexual, hermaphrodite, extra hands, fused fingers, poorly drawn hands, long neck, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, bad anatomy, bad proportions, malformed limbs, extra limbs, cloned face, disfigured, more than 2 nipples, missing arms, missing legs, extra arms, (extra legs), extra toes, missing fingers, deformed fingers, panties, panty, thong, red eyes, fake tits, christmas elf, elf cap, cap, hat, (((multiple sets of ears:1.3))), (bad-hands-5:1.2), nipples, focus on breast, lowres, cropped, scars, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, asian appearance, japan appearance, scars on the body",
    "nsfw": False,
    "performance": "quality",
    #ENABLED PROMT! - it can be change - see more on pornworks.com
    "prompt": "1girl, underboob, skindentation, long hair, breasts, (huge breasts:1.2), (beautiful face:1.2), (makeup, lipstick, blush, eyeliner:.7), (colorful:.6), realistic, sweaty skin, perfect body, " + random.choice(girls),
    "resources": [],
    #SAMPLER (generator) - it can be change, see more on pornworks.com
    #"samplerName": "DPM++ 2S a Karras",
    "sharpness": 5,
    "ratio": "1x1",
    "size": "1024x1024", 
}

def set_boobs(num_retries = 15):
    for attempt_no in range(num_retries):
        try:
            r = requests.post(os.getenv("BOOBS_API_URL") + "/text2image", headers=header, json=data)
            print(r.text)
            t = json.loads(r.text)
            j = t["id"]
            return j
        except:
            if attempt_no < (num_retries - 1):
                time.sleep(60) #WAIT 60sec - DONT SPAM API!
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
                r = requests.get(os.getenv("BOOBS_API_GENERATOR_URL") + get_id +  "/state", headers=header)
                print(r.text)
                t = json.loads(r.text)
                local_file_name = os.getenv("PATH_FOR_IMG") + get_id + ".png"
                img_url = t["results"]["image"]
                print(img_url)
                r_img = requests.get(img_url, stream=True, headers=header)
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
