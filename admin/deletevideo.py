from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.videos_db import delete_video

@app.on_message(filters.command("deletevideo") & admin_filter)
async def deletevideo_cmd(client, message):

    try:
        msg_id = int(message.command[1])

    except:
        return await message.reply_text(
            "/deletevideo msg_id"
        )

    await delete_video(msg_id)

    await message.reply_text(
        "🗑 Video Deleted"
    )
