from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.videos_db import add_demo

@app.on_message(filters.command("adddemo") & admin_filter)
async def adddemo(client, message):

    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "⚠️ Reply To Demo Video"
        )

    await add_demo(
        reply.chat.id,
        reply.id
    )

    await message.reply_text(
        "✅ Demo Video Added"
    )
