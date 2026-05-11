from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.mongo import users

@app.on_message(filters.command("users") & admin_filter)
async def users_list(client, message):

    total = await users.count_documents({})

    await message.reply_text(
        f"👥 Total Users : {total}"
    )
