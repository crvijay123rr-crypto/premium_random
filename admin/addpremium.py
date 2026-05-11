from pyrogram import filters

from bot import app
from config import PLAN_PRICE

from database.users_db import (
    is_premium,
    get_user
)


@app.on_message(filters.command("buy"))
async def buy(client, message):

    user_id = message.from_user.id

    # CHECK PREMIUM
    premium = await is_premium(user_id)

    # ALREADY PREMIUM
    if premium:

        user = await get_user(user_id)

        return await message.reply_text(
            f"""
╔════════════════════╗
   👑 PREMIUM ACTIVE 👑
╚════════════════════╝

✅ You Are Already A Premium Member

📅 Expiry :
{user.get('expiry')}

⚡ Daily Limit : 100 Videos
🛡 Protected Content Enabled

🔥 Enjoy Unlimited Premium Access
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
