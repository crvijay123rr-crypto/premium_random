from pyrogram import filters

from bot import app
from config import PREMIUM_CHANNEL

from admin.admin import admin_filter

from database.videos_db import add_video


@app.on_message(filters.command("sync") & admin_filter)
async def sync_channel(client, message):

    count = 0

    await message.reply_text(
        "🔄 Sync Started..."
    )

    async for msg in app.get_chat_history(PREMIUM_CHANNEL):

        try:

            if msg.video:

                await add_video(msg.id)

                count += 1

        except Exception as e:

            print(e)

    await message.reply_text(
        f"✅ Synced {count} Videos"
    )
