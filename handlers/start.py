from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import app
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


START_PIC = "assets/banner.jpg"


@app.on_message(filters.command("start"))
async def start(client, message):

    try:
        await add_user(message.from_user.id)

    except Exception as e:
        print(f"ADD USER ERROR: {e}")

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 GET VIDEOS", callback_data="videos")],
        [InlineKeyboardButton("🎁 FREE DEMO", callback_data="demo")],
        [InlineKeyboardButton("💳 BUY PREMIUM", callback_data="buy")],
        [InlineKeyboardButton("📊 MY PLAN", callback_data="myplan")],
        [InlineKeyboardButton("☎ SUPPORT", url="http://t.me/Contact_45bot")]
    ])

    await message.reply_photo(
        photo=START_PIC,
        caption=START_TEXT,
        reply_markup=buttons
    )
