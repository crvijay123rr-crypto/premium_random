from pyrogram import filters

from bot import app
from config import DEMO_CHANNEL

from admin.admin import admin_filter

from database.videos_db import add_demo_video


@app.on_message(filters.command("syncdemo") & admin_filter)
async def sync_demo(client, message):

    count = 0

    await message.reply_text(
        "🔄 Demo Sync Started..."
    )

    async for msg in app.get_chat_history(DEMO_CHANNEL):

        try:

            if msg.video:

                await add_demo_video(msg.id)

                count += 1

        except Exception as e:

            print(e)

    await message.reply_text(
        f"✅ Synced {count} Demo Videos"
    )
