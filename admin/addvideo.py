from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.videos_db import add_video

@app.on_message(filters.command("addvideo") & admin_filter)
async def addvideo(client, message):

    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "⚠️ Reply To Video"
        )

    await add_video(
        reply.chat.id,
        reply.id
    )

    await message.reply_text(
        "✅ Premium Video Added"
    )
