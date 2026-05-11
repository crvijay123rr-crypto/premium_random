from pyrogram import filters

from bot import app

from database.users_db import (
    get_user,
    is_premium
)


@app.on_message(filters.command("myplan"))
async def myplan(client, message):

    user_id = message.from_user.id

    user = await get_user(user_id)

    # USER NOT FOUND
    if not user:

        return await message.reply_text(
            "❌ User not found.\nPlease send start first."
        )

    # PREMIUM CHECK
    premium = await is_premium(user_id)

    # NO PREMIUM
    if not premium:

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
    total_received = user.get(
        "total_received",
        0
    )

    text = f"""
╔════════════════════╗
      👑 PREMIUM ACTIVE 👑
╚════════════════════╝

📅 Expiry Date :
{user.get('expiry')}

━━━━━━━━━━━━━━━━━━━

🎥 Videos Used Today :
{user.get('used_today', 0)}/1

📦 Total Videos Received :
{total_received}

━━━━━━━━━━━━━━━━━━━

🚀 Enjoy Premium Access
"""

    await message.reply_text(text)
