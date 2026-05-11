from pyrogram import filters

from bot import app

from database.users_db import (
    get_user
)

@app.on_message(filters.command("myplan"))
async def myplan(client, message):

    user = await get_user(message.from_user.id)

    if not user["premium"]:
        return await message.reply_text(
            "❌ No Active Premium"
        )

    text = f"""
👑 PREMIUM ACTIVE

📅 Expiry :
{user['expiry']}

🎥 Used Today :
{user['used_today']}/100
"""

    await message.reply_text(text)# Plan handler
