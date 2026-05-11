from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.users_db import ban_user

@app.on_message(filters.command("ban") & admin_filter)
async def ban(client, message):

    try:
        user_id = int(message.command[1])

    except:
        return await message.reply_text(
            "/ban user_id"
        )

    await ban_user(user_id)

    await message.reply_text(
        "✅ User Banned"
    )# Ban system
