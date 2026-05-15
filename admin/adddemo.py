from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.videos_db import add_demo


@app.on_message(filters.command("adddemo") & admin_filter)
async def adddemo(client, message):

    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "⚠️ Reply To Demo Video"
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

        added = await add_demo(
            reply.chat.id,
            reply.id
        )

        # ALREADY EXISTS
        if not added:
            return await message.reply_text(
                "⚠️ Demo Already Added"
            )

        await message.reply_text(
            "✅ Demo Video Added"
        )

    except Exception as e:

        await message.reply_text(
            f"❌ Error:\n{e}"
        )
