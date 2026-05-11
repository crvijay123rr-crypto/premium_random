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
            """
╔════════════════════╗
      ❌ NO PREMIUM ❌
╚════════════════════╝

💎 You Don't Have Any
Active Premium Plan

📩 DM FAST :
@Contact_45bot
"""
        )

    # TOTAL RECEIVED
    total_received = user.get("total_received", 0)

    text = f"""
╔════════════════════╗
      👑 MY PREMIUM 👑
╚════════════════════╝

📅 Expiry Date :
{user.get('expiry', 'Not Set')}

━━━━━━━━━━━━━━━━━━━

🎥 Videos Used Today :
{user.get('used_today', 0)}/100

📦 Total Videos Received :
{total_received}

━━━━━━━━━━━━━━━━━━━

🚀 Enjoy Premium Access
"""

    await message.reply_text(text)
