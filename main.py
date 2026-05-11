from pyrogram import Client
from config import *

app = Client(
    "PremiumBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

import handlers.start
import handlers.videos
import handlers.demo
import handlers.buy
import handlers.myplan
import handlers.support
import handlers.referral
import handlers.redeem
import handlers.callbacks
import handlers.force_sub

import admin.admin
import admin.broadcast
import admin.stats
import admin.ban
import admin.unban

print("BOT STARTED")

app.run()
