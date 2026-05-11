from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.users_db import unban_user

@app.on_message(filters.command("unban") & admin_filter)
async def unban(client, message):

    try:
        user_id = int(message.command[1])

    except:
        return await message.reply_text(
            "/unban user_id"
        )

    await unban_user(user_id)

    await message.reply_text(
        "✅ User Unbanned"
    )# Unban system
