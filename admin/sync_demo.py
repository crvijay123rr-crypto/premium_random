from pyrogram import filters

from bot import app, userbot
from config import DEMO_CHANNEL

from admin.admin import admin_filter

from database.videos_db import add_demo


@app.on_message(filters.command("syncdemo") & admin_filter)
async def sync_demo(client, message):

    count = 0

    await message.reply_text(
        "🔄 Demo Sync Started..."
    )

    # USERBOT HISTORY READ
    async for msg in userbot.get_chat_history(DEMO_CHANNEL):

        try:

            if msg.video:

                await add_demo(
                    DEMO_CHANNEL,
                    msg.id
                )

                count += 1

                print(f"Demo Synced: {msg.id}")

        except Exception as e:

            print(e)

    await message.reply_text(
        f"✅ Synced {count} Demo Videos"
    )
