#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : s0rkin
# Created Date: Aug 20, 2023
# Links       : https://github.com/s0rkin/
# version ='1.2'
# ---------------------------------------------------------------------------

import json
import os
import random
import time
from pathlib import Path

from dotenv import load_dotenv

# Load file .env config.
load_dotenv()

BASE_URL = os.getenv("BOOBS_URL", "https://pornworks.com").rstrip("/")
API_URL = os.getenv("BOOBS_API_URL", f"{BASE_URL}/api/v2/generate").rstrip("/")
GENERATOR_URL = os.getenv(
    "BOOBS_API_GENERATOR_URL", f"{BASE_URL}/api/v2/generations/"
).rstrip("/") + "/"
GENERATOR_PAGE_URL = f"{BASE_URL}/en/generate/image"

# Girls hair for random.
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
    "White hair",
]

# Models can be changed; see PornWorks for currently available free models.
models = ["nude_people", "real_porn_pony", "hardcore_fantasy"]

# Main data for POST.
data = {
    "cfgScale": 7,
    "checkpoint": random.choice(models),
    "fast": False,
    "hr": False,
    "negativePrompt": "(vaginal sex:1.5), painting, vagina, sketches, lowers, monochrome, grayscale, skin spots, acnes, skin blemishes, age spot, (outdoor:1.2), fat, mole, g_deepnegative_v1_75t, (((poorly drawn hands))), (worst quality:2), (low quality:2), (normal quality:2), cat ears, elf ears, tail, wings, pointed ears, lowres, extra glans, extra fingers, fewer fingers, strange fingers, bad hand, jpeg, artifacts, signature, ugly, pregnant, vore, duplicate, morbid, mutilated, tranny, trans, trannsexual, hermaphrodite, extra hands, fused fingers, long neck, mutated hands, poorly drawn face, mutation, deformed, blurry, bad anatomy, bad proportions, malformed limbs, extra limbs, cloned face, disfigured, more than 2 nipples, missing arms, missing legs, extra arms, (extra legs), extra toes, missing fingers, deformed fingers, panties, panty, thong, red eyes, fake tits, christmas elf, elf cap, cap, hat, (((multiple sets of ears:1.3))), (bad-hands-5:1.2), nipples, focus on breast, cropped, scars, out of frame, dehydrated, gross proportions, too many fingers, asian appearance, japan appearance, scars on the body",
    "nsfw": True,
    "performance": "express",
    "prompt": random.choice(girls) + ", 1girl, underboob, skin indentation, long hair, breasts, (large breasts:1.1), (beautiful face:1.2), (makeup, lipstick, blush, eyeliner:0.8), sweaty skin, perfect body, nude, ultra detailed skin, ultra detailed face, natural lighting, (photorealistic:1.5), 8k, UHD, random background place, topless nude, light smile, realistic detailed eyes, ealistic detailed face, realistic detailed tan skin, nose freckles, full body, cute, ultra realistic, masterpiece, extremely sensual, perfect boobs, white, wet body, wet hair, perfect fingers and hands, amateur photograph, intricate details, perfect tits, shirt, pale skin, side view, panties aside, detailed background",
    "resources": [],
    "sharpness": 5,
    "ratio": "1x1",
    "size": "1024x1024",
}


class PornWorksError(RuntimeError):
    pass


class CloudflareChallengeError(PornWorksError):
    pass


class PornWorksApiError(PornWorksError):
    pass


def _is_cloudflare_challenge(status, body):
    body_lower = body.lower()
    return status == 403 and (
        "just a moment" in body_lower
        or "cf-chl-" in body_lower
        or "cloudflare" in body_lower
    )


class CloakBrowserClient:
    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        cache_path = project_root / ".cloakbrowser-cache"
        os.environ.setdefault("CLOAKBROWSER_CACHE_DIR", str(cache_path))

        try:
            from cloakbrowser import launch_persistent_context
            from playwright.sync_api import TimeoutError
        except ImportError as exc:
            raise PornWorksError(
                "CloakBrowser is not installed; run .venv/bin/python -m pip install -r requirements.txt"
            ) from exc

        self._timeout_error = TimeoutError
        profile_path = Path(
            os.getenv("BOOBS_BROWSER_PROFILE", project_root / ".cloakbrowser-profile")
        )
        profile_path.mkdir(parents=True, exist_ok=True)

        try:
            self.context = launch_persistent_context(
                profile_path,
                headless=os.getenv("BOOBS_BROWSER_HEADLESS", "false").lower()
                not in {"0", "false", "no"},
                proxy=os.getenv("PROXY_HOST") or None,
                geoip=True,
                humanize=True,
                args=["--fingerprint-storage-quota=5000"],
            )
        except Exception as exc:
            raise PornWorksError(
                "Could not launch CloakBrowser Chromium; run it through xvfb-run"
            ) from exc

        self.page = self.context.pages[0] if self.context.pages else self.context.new_page()
        self._open_generator()

    def _open_generator(self):
        timeout_ms = int(os.getenv("BOOBS_BROWSER_TIMEOUT_MS", "90000"))
        try:
            self.page.goto(
                GENERATOR_PAGE_URL,
                wait_until="domcontentloaded",
                timeout=timeout_ms,
            )
        except self._timeout_error:
            # Cloudflare may continue navigating while it verifies the browser.
            pass

        deadline = time.monotonic() + (timeout_ms / 1000)
        clear_since = None
        while time.monotonic() < deadline:
            title = self.page.title().lower()
            has_turnstile = any(
                "challenges.cloudflare.com" in frame.url for frame in self.page.frames
            )
            if "just a moment" not in title and not has_turnstile:
                clear_since = clear_since or time.monotonic()
                if time.monotonic() - clear_since >= 3:
                    return
            else:
                clear_since = None
            self.page.wait_for_timeout(1000)
        if any("challenges.cloudflare.com" in frame.url for frame in self.page.frames):
            raise CloudflareChallengeError(
                "Cloudflare requires interactive Turnstile verification for the "
                "persistent Chromium profile"
            )
        raise CloudflareChallengeError(
            "Cloudflare challenge did not finish in Chromium"
        )

    def close(self):
        self.context.close()

    def request_json(self, method, url, payload=None):
        result = self.page.evaluate(
            """
            async ({method, url, payload}) => {
                const options = {
                    method,
                    credentials: "include",
                    headers: {
                        "Accept": "application/json; charset=utf-8",
                        "Content-Type": "application/json; charset=UTF-8",
                        "X-Requested-With": "XMLHttpRequest"
                    }
                };
                if (payload !== null) options.body = JSON.stringify(payload);
                const response = await fetch(url, options);
                return {status: response.status, body: await response.text()};
            }
            """,
            {"method": method, "url": url, "payload": payload},
        )
        if _is_cloudflare_challenge(result["status"], result["body"]):
            raise CloudflareChallengeError(
                "PornWorks challenged the API request inside Chromium"
            )
        if result["status"] >= 400:
            raise PornWorksApiError(
                f"PornWorks API returned HTTP {result['status']}: {result['body'][:200]}"
            )
        try:
            return json.loads(result["body"])
        except ValueError as exc:
            raise PornWorksError("PornWorks API returned non-JSON content") from exc

    def download(self, url):
        response = self.context.request.get(url, timeout=60000)
        if not response.ok:
            raise PornWorksError(f"Image download returned HTTP {response.status}")
        return response.body()


def set_boobs(client, num_retries=3):
    for attempt_no in range(num_retries):
        try:
            response = client.request_json("POST", f"{API_URL}/text2image", data)
            generation_id = response.get("id")
            if not generation_id:
                raise PornWorksError("PornWorks response does not contain a generation id")
            return generation_id
        except CloudflareChallengeError:
            raise
        except PornWorksApiError:
            raise
        except Exception as exc:
            if attempt_no == num_retries - 1:
                raise PornWorksError(
                    f"Could not start generation after {num_retries} attempts"
                ) from exc
            print(f"set_boobs attempts left: {num_retries - attempt_no - 1}: {exc}")
            time.sleep(10)


def get_boobs(client, generation_id, num_retries=90):
    for attempt_no in range(num_retries):
        try:
            response = client.request_json(
                "GET", f"{GENERATOR_URL}{generation_id}/state"
            )
            image_url = response.get("results", {}).get("image")
            if not image_url:
                if attempt_no < num_retries - 1:
                    time.sleep(15)
                    continue
                raise PornWorksError("Generation did not produce an image in time")

            output_path = Path(os.getenv("PATH_FOR_IMG", ".")) / f"{generation_id}.png"
            output_path.write_bytes(client.download(image_url))
            return str(output_path)
        except CloudflareChallengeError:
            raise
        except PornWorksApiError:
            raise
        except Exception as exc:
            if attempt_no == num_retries - 1:
                raise PornWorksError(
                    f"Could not fetch generation after {num_retries} attempts"
                ) from exc
            print(f"get_boobs attempts left: {num_retries - attempt_no - 1}: {exc}")
            time.sleep(15)


def generate_boobs():
    client = None
    try:
        client = CloakBrowserClient()
        generation_id = set_boobs(client)
        return get_boobs(client, generation_id)
    except Exception as exc:
        print(f"PornWorks error: {exc}")
        return os.getenv("IMG_EXCEPT")
    finally:
        if client:
            client.close()


get_boobs_file = generate_boobs()
