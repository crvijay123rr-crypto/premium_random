from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.mongo import users

@app.on_message(filters.command("premiums") & admin_filter)
async def premiums(client, message):

    total = await users.count_documents({
        "premium": True
    })

    await message.reply_text(
        f"👑 Premium Users : {total}"
    )
