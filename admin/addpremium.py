from pyrogram import filters

from bot import app

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

🔥 Enjoy Unlimited Premium Access
⚡ Daily 100 Videos Available
🛡 Protected Content Enabled
"""
        )

    # BUY MESSAGE
    await message.reply_text(
        """
╔════════════════════╗
      💎 BUY PREMIUM 💎
╚════════════════════╝

🔥 Unlock Premium Features

⚡ Daily 100 Videos
🛡 Protected Content
🎬 Unlimited Access

━━━━━━━━━━━━━━━━━━━

💰 Price : ₹200 / 30 Days

📩 Contact Admin :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Activate Premium Instantly
"""
    )
