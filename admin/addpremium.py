from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.users_db import activate_premium

@app.on_message(filters.command("addpremium") & admin_filter)
async def addpremium(client, message):

    try:
        user_id = int(message.command[1])

    except:
        return await message.reply_text(
            "/addpremium user_id"
        )

    await activate_premium(user_id)

    await message.reply_text(
        "✅ Premium Activated"
    )
