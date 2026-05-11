from pyrogram import Client
from config import *

app = Client(
    "PremiumBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
