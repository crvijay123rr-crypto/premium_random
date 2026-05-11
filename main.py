from pyrogram import filters

from bot import app, userbot

# =========================
# START USERBOT
# =========================
userbot.start()

# =========================
# USER HANDLERS
# =========================
import handlers.start
import handlers.videos
import handlers.demo
import handlers.buy
import handlers.myplan
import handlers.callbacks

# OPTIONAL
import handlers.support
import handlers.referral
import handlers.redeem
import handlers.force_sub


# =========================
# ADMIN HANDLERS
# =========================
import admin.addvideo
import admin.adddemo
import admin.addpremium
import admin.broadcast
import admin.ban
import admin.unban
import admin.stats
import admin.sync_channel
import admin.sync_demo
import admin.syncnew


print("🚀 BOT STARTED SUCCESSFULLY")


# =========================
# PING COMMAND
# =========================
@app.on_message(filters.command("ping"))
async def ping(_, message):

    await message.reply_text(
        """
╔════════════════════╗
        🏓 PONG 🏓
╚════════════════════╝

✅ Bot Is Running Successfully
⚡ Server Status : Online
🚀 Speed : Fast
"""
    )


# =========================
# START BOT
# =========================
app.run()
