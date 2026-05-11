from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.mongo import users

@app.on_message(filters.command("broadcast") & admin_filter)
async def broadcast(client, message):

    if not message.reply_to_message:
        return await message.reply_text(
            "⚠️ Reply To Message"
        )

    success = 0
    failed = 0

    all_users = users.find({})

    async for user in all_users:

        try:

            await message.reply_to_message.copy(
                user["user_id"]
            )

            success += 1

        except:

            failed += 1

    text = f"""
📢 BROADCAST DONE

✅ Success : {success}
❌ Failed : {failed}
"""

    await message.reply_text(text)# Broadcast system
