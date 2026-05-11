from pyrogram import filters

from bot import app

# USER HANDLERS
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

# ADMIN HANDLERS
import admin.addvideo
import admin.adddemo
import admin.addpremium
import admin.broadcast
import admin.ban
import admin.unban
import admin.stats

# SYNC SYSTEM
import admin.sync_channel
import admin.sync_demo


print("🚀 BOT STARTED SUCCESSFULLY")


# PING COMMAND
@app.on_message(filters.command("ping"))
async def ping(_, message):

    await message.reply_text(
        "🏓 Pong!"
    )


app.run()
