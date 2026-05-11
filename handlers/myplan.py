from pyrogram import filters

from bot import app

from database.users_db import get_user


@app.on_message(filters.command("myplan"))
async def myplan(client, message):

    user = await get_user(message.from_user.id)

    # USER NOT FOUND
    if not user:
        return await message.reply_text(
            "❌ User not found.\nPlease send /start first."
        )

    # NO PREMIUM
    if not user.get("premium"):
        return await message.reply_text(
            "❌ No Active Premium"
        )

    text = f"""
👑 PREMIUM ACTIVE

📅 Expiry :
{user.get('expiry', 'Not Set')}

🎥 Used Today :
{user.get('used_today', 0)}/100
"""

    await message.reply_text(text)
