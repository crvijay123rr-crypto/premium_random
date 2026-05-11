from pyrogram import filters

from bot import app
from config import PLAN_PRICE
from admin.admin import admin_filter

from database.users_db import (
    is_premium,
    get_user,
    activate_premium
)


# =========================
# BUY COMMAND
# =========================
@app.on_message(filters.command("buy"))
async def buy(client, message):

    user_id = message.from_user.id

    # CHECK PREMIUM
    premium = await is_premium(user_id)

    # ALREADY PREMIUM
    if premium:

        user = await get_user(user_id)

        expiry = user.get("expiry")

        return await message.reply_text(
            f"""
╔════════════════════╗
   👑 PREMIUM ACTIVE 👑
╚════════════════════╝

✅ You Are Already A Premium Member

📅 Expiry Date :
{expiry.strftime("%d-%m-%Y")}

━━━━━━━━━━━━━━━━━━━

⚡ Daily Limit : 100 Videos
🛡 Protected Content Enabled
🎬 Unlimited Premium Access

━━━━━━━━━━━━━━━━━━━

🔥 Enjoy Premium Features
"""
        )

    # BUY MESSAGE
    await message.reply_text(
        f"""
╔════════════════════╗
      💎 BUY PREMIUM 💎
╚════════════════════╝

🔥 Unlock Premium Features

⚡ Daily 100 Videos
🛡 Protected Content
🎬 Unlimited Access

━━━━━━━━━━━━━━━━━━━

📅 Plan : Custom Days Available

💰 Price Starts From :
₹{PLAN_PRICE}

📩 Contact Admin :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Activate Premium Instantly
"""
    )


# =========================
# ADD PREMIUM COMMAND
# =========================
@app.on_message(filters.command("addpremium") & admin_filter)
async def addpremium(client, message):

    # CHECK ARGUMENT
    if len(message.command) < 2:

        return await message.reply_text(
            "❌ Usage : /addpremium user_id"
        )

    # GET USER ID
    try:
        user_id = int(message.command[1])

    except:
        return await message.reply_text(
            "❌ Invalid User ID"
        )

    # ACTIVATE PREMIUM
    await activate_premium(user_id)

    # ADMIN SUCCESS MESSAGE
    await message.reply_text(
        f"""
╔════════════════════╗
    ✅ PREMIUM ADDED ✅
╚════════════════════╝

👤 User ID :
{user_id}

🔥 Premium Activated Successfully
"""
    )

    # USER MESSAGE
    try:

        await app.send_message(
            user_id,
            """
╔══════════════════╗
     👑 PREMIUM ACTIVE 👑
╚══════════════════╝

🎉 Congratulations!

💎 Your Premium Has Been Activated Successfully

⚡ Daily Limit : 100 Videos
🛡 Protected Content Enabled

🔥 Enjoy Unlimited Premium Access
"""
        )

    except Exception as e:

        print(f"USER MESSAGE ERROR : {e}")
