from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.videos_db import add_video


@app.on_message(filters.command("addvideo") & admin_filter)
async def addvideo(client, message):

    reply = message.reply_to_message

    # CHECK REPLY
    if not reply:

        return await message.reply_text(
            "⚠️ Reply To A Video Message"
        )

    # ONLY VIDEO ALLOWED
    if not reply.video:

        return await message.reply_text(
            "❌ Only Video Messages Allowed"
        )

    # SAVE VIDEO
    await add_video(
        reply.chat.id,
        reply.id
    )

    # SUCCESS
    await message.reply_text(
        """
╔════════════════════╗
     ✅ VIDEO ADDED ✅
╚════════════════════╝

🎬 Premium Video Saved Successfully
"""
    )
