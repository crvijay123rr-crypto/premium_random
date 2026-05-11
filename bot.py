from pyrogram import Client
from config import *

# BOT CLIENT
app = Client(
    "PremiumBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,

    workers=200,
    sleep_threshold=30,
    no_updates=False
)

# USERBOT CLIENT
userbot = Client(
    "UserbotSession",
    api_id=API_ID,
    api_hash=API_HASH,

    workers=100,
    sleep_threshold=30,
    no_updates=True
)
