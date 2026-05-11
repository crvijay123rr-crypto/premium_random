from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.videos_db import add_demo


@app.on_message(filters.command("adddemo") & admin_filter)
async def adddemo(client, message):

    reply = message.reply_to_message

    # CHECK REPLY
    if not reply:

        return await message.reply_text(
            "⚠️ Reply To A Demo Video"
        )

    # ONLY VIDEO ALLOWED
    if not reply.video:

        return await message.reply_text(
            "❌ Only Video Messages Allowed"
        )

    # SAVE DEMO VIDEO
    await add_demo(
        reply.chat.id,
        reply.id
    )

    # SUCCESS MESSAGE
    await message.reply_text(
        """
╔════════════════════╗
    ✅ DEMO ADDED ✅
╚════════════════════╝

🎁 Demo Video Saved Successfully
"""
    )
