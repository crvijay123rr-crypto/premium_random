# =========================
# RESET DEMO COMMAND
# FILE : admin/resetdemo.py
# =========================

import asyncio

from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.mongo import users


@app.on_message(filters.command("resetdemo") & admin_filter)
async def reset_demo_command(client, message):

    reset_msg = await message.reply_text(
        """
╔══════════════════════╗
      ♻️ RESETTING ♻️
╚══════════════════════╝

⚡ Resetting All Users
Free Demo Access...

📡 Sending Notifications...
"""
    )

    # RESET ALL USERS
    await users.update_many(
        {},
        {
            "$set": {
                "demo_used": 0,
                "last_demo_date": None
            }
        }
    )

    # GET USERS
    all_users = users.find({})

    sent = 0
    failed = 0

    # BROADCAST
    async for user in all_users:

        try:

            await app.send_message(
                chat_id=user["user_id"],
                text="""
╔══════════════════════╗
      🎉 DEMO RESET 🎉
╚══════════════════════╝

🔥 Your Free Demo
Has Been Reset Successfully

🎬 Use /demo Now
And Enjoy Fresh Content
"""
            )

            sent += 1

            await asyncio.sleep(0.1)

        except Exception:
            failed += 1

    # FINAL STATUS
    await reset_msg.edit_text(
        f"""
╔══════════════════════╗
      ✅ RESET DONE ✅
╚══════════════════════╝

🎬 All Demo Users Reset
Successfully

📢 Notifications Sent :
{sent}

❌ Failed Users :
{failed}

🚀 Everyone Can Use
/demo Again
"""
    )
