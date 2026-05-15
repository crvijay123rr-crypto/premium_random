from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.videos_db import add_video


@app.on_message(filters.command("addvideo") & admin_filter)
async def addvideo(client, message):

    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "⚠️ Reply To A Video"
        )

    # EMPTY MESSAGE CHECK
    if reply.empty:
        return await message.reply_text(
            "❌ Empty Message"
        )

    # CHECK VIDEO
    if not (
        reply.video
        or reply.document
        or reply.animation
    ):
        return await message.reply_text(
            "❌ Only Video Files Allowed"
        )

    try:

        added = await add_video(
            reply.chat.id,
            reply.id
        )

        # ALREADY EXISTS
        if not added:
            return await message.reply_text(
                "⚠️ Video Already Added"
            )

        await message.reply_text(
            "✅ Premium Video Added"
        )

    except Exception as e:

        await message.reply_text(
            f"❌ Error:\n{e}"
        )
