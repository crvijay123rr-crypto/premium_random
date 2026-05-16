from pyrogram import filters

from bot import app

from config import PREMIUM_IDS, DAILY_LIMIT

from database.users_db import (
    get_user,
    is_premium
)


@app.on_message(filters.command("myplan"))
async def myplan(client, message):

    if not message.from_user:
        return

    user_id = int(message.from_user.id)

    print("USER_ID =", user_id)
    print("PREMIUM_IDS =", PREMIUM_IDS)
    print("MATCH =", user_id in PREMIUM_IDS)

    # =========================
    # GET USER
    # =========================
    user = await get_user(user_id)

    # =========================
    # PREMIUM CHECK
    # =========================
    premium = False

    # CONFIG PREMIUM IDS
    if user_id in list(map(int, PREMIUM_IDS)):
        premium = True

    # DATABASE PREMIUM
    elif user:
        premium = await is_premium(user_id)

    # =========================
    # NO PREMIUM
    # =========================
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

    # =========================
    # CUSTOM PREMIUM USER
    # =========================
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

    # =========================
    # TOTAL RECEIVED
    # =========================
    total_received = user.get(
        "total_received",
        0
    )

    expiry = user.get("expiry")

    # =========================
    # EXPIRY TEXT
    # =========================
    if user_id in list(map(int, PREMIUM_IDS)):
        expiry_text = "Unlimited"

    else:
        expiry_text = expiry

    # =========================
    # MESSAGE
    # =========================
    text = f"""
╔════════════════════╗
      👑 PREMIUM ACTIVE 👑
╚════════════════════╝

📅 Expiry Date :
{expiry_text}

━━━━━━━━━━━━━━━━━━━

🎥 Videos Used Today :
{user.get('used_today', 0)}/{DAILY_LIMIT}

📦 Total Videos Received :
{total_received}

━━━━━━━━━━━━━━━━━━━

🚀 Enjoy Premium Access
"""

    await message.reply_text(text)
