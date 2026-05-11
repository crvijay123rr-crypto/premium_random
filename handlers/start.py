from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from main import app
from database.users_db import add_user

START_TEXT = """
╔════════════════╗
   👑 PREMIUM HUB 👑
╚════════════════╝

🔥 Unlimited Random Videos
⚡ Daily 100 Videos
🛡 Protected Content
💎 Monthly VIP Access
"""

@app.on_message(filters.command("start"))
async def start(client, message):

    await add_user(message.from_user.id)

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 GET VIDEOS", callback_data="videos")],
        [InlineKeyboardButton("🎁 FREE DEMO", callback_data="demo")],
        [InlineKeyboardButton("💳 BUY PREMIUM", callback_data="buy")],
        [InlineKeyboardButton("📊 MY PLAN", callback_data="myplan")],
        [InlineKeyboardButton("☎ SUPPORT", url="https://t.me/yourusername")]
    ])

    await message.reply_text(
        START_TEXT,
        reply_markup=buttons
    )
