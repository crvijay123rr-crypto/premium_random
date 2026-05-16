from pyrogram import filters

from bot import app

from database.users_db import (
    get_user,
    is_premium
)


@app.on_message(filters.command("myplan"))
async def myplan(client, message):

    user_id = message.from_user.id

    # GET USER
    user = await get_user(user_id)

    # PREMIUM CHECK
    premium = await is_premium(user_id)

    # DATABASE PREMIUM CHECK
    if not premium and user:
        premium = user.get("premium", False)

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

    # USER NOT FOUND BUT PREMIUM ID
    if not user:

        return await message.reply_text(
            """
╔════════════════════╗
      👑 PREMIUM ACTIVE 👑
╚════════════════════╝

♾ Unlimited Premium Access

🚀 Custom Premium ID User
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
