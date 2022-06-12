## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAE-z8ix-ebgerK9nWjM00bUsG6fmE9O3_4GNZkdMpbY6M2oejHoZMzTWj8mmgWg3iaE59IZmoOM2mFfP64O8zGlU3M325CftkhwecSLPmm4Zva80K--GdrMXEbCPwSqjFfrucR1mWlOUHRJC2pzuhicIWq8OfCIIkKOg_KfnNANnv6slNwRLfK3TTwAbyovzcSQtm530k1j5tyBvP6OG76oa0GIjI6Yr7RcOrlUEyHSKuDs7I55-cMGp0cSw5YGe7xwCOf3QAmfBKp-xIA6-ez5UsuTRTRUnVPYnXEPc4mW8-fx3OTYHoLSD_5ZAAjDrCDGgW6yYff4O7o0DImGowyJvCIQgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5127235535:AAFp9gVXYvC3G6yPq12ejuRhi8Q-Y2_HEAM")
BOT_NAME = getenv("BOT_NAME", "felix")
API_ID = int(getenv("API_ID", "19680685"))
API_HASH = getenv("API_HASH", "35c8346d7d35af39fcc9204493970277")
OWNER_NAME = getenv("OWNER_NAME", "hadi")
OWNER_USERNAME = getenv("OWNER_USERNAME", "jbbbbf")
ALIVE_NAME = getenv("ALIVE_NAME", "hadi")
BOT_USERNAME = getenv("BOT_USERNAME", "Ftgggg4_9bot")
OWNER_ID = getenv("OWNER_ID", "5049024596")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "abfm00")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "abfm5")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "abfm5")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5049024596").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
