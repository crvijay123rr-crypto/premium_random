from pyrogram import filters
from bot import app

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

print("🚀 BOT STARTED SUCCESSFULLY")


@app.on_message(filters.command("ping"))
async def ping(_, message):
    await message.reply_text("🏓 Pong!")


app.run()
