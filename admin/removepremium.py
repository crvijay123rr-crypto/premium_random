from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.users_db import remove_premium


@app.on_message(filters.command("removepremium") & admin_filter)
async def removepremium(client, message):

    try:
        user_id = int(message.command[1])

    except:
        return await message.reply_text(
            "❌ Usage : /removepremium user_id"
        )

    await remove_premium(user_id)

    await message.reply_text(
        "✅ Premium Removed Successfully"
    )
