from pyrogram import filters

from bot import app
from config import PLAN_PRICE

from database.users_db import is_premium


@app.on_message(filters.command("buy"))
async def buy(client, message):

    user_id = message.from_user.id

    # CHECK PREMIUM
    premium = await is_premium(user_id)

    # ALREADY PREMIUM
    if premium:

        return await message.reply_text(
            """
╔════════════════════╗
   👑 PREMIUM ACTIVE 👑
╚════════════════════╝

✅ You Are Already A Premium Member

⚡ Daily Limit : 100 Videos
🛡 Protected Content Enabled

🔥 Enjoy Unlimited Premium Access
"""
        )

    # BUY MESSAGE
    text = f"""
╔════════════════════╗
      💎 BUY PREMIUM 💎
╚════════════════════╝

📅 Duration : 30 Days
🎥 Daily Limit : 100 Videos

━━━━━━━━━━━━━━━━━━━

💰 Price : ₹{PLAN_PRICE}

❌ UPI Payment Not Available

✅ Only PhonePe Gift Card Accepted

📤 Send Payment Screenshot To:
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Get Instant Premium Access
"""

    await message.reply_text(text)
