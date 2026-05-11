from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.users_db import activate_premium


@app.on_message(filters.command("addpremium") & admin_filter)
async def addpremium(client, message):

    try:
        user_id = int(message.command[1])

    except:
        return await message.reply_text(
            "❌ Usage : /addpremium user_id"
        )

    # ACTIVATE PREMIUM
    await activate_premium(user_id)

    # ADMIN REPLY
    await message.reply_text(
        "✅ Premium Activated Successfully"
    )

    # USER MESSAGE
    try:

        text = f"""
╔══════════════════╗
     👑 PREMIUM ACTIVE 👑
╚══════════════════╝

🎉 Congratulations!

💎 Your Premium Has Been Activated Successfully

⚡ Daily Limit : 100 Videos
📅 Plan : 30 Days
🛡 Protected Content Enabled

🔥 Enjoy Unlimited Premium Access
"""

        await app.send_message(
            chat_id=user_id,
            text=text
        )

    except Exception as e:

        print(f"USER MESSAGE ERROR : {e}")
