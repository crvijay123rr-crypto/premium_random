from pyrogram import filters

from bot import app, userbot
from config import PREMIUM_CHANNEL

from admin.admin import admin_filter

from database.videos_db import (
    add_video,
    get_all_videos
)


@app.on_message(filters.command("sync") & admin_filter)
async def sync_channel(client, message):

    count = 0

    await message.reply_text(
        "🔄 Sync Started..."
    )

    # OLD VIDEOS LOAD
    old_videos = await get_all_videos()

    old_ids = [x["msg_id"] for x in old_videos]

    # USERBOT HISTORY READ
    async for msg in userbot.get_chat_history(PREMIUM_CHANNEL):

        try:

            if msg.video:

                # SKIP DUPLICATE
                if msg.id in old_ids:
                    continue

                await add_video(
                    PREMIUM_CHANNEL,
                    msg.id
                )

                count += 1

                # PROGRESS
                if count % 100 == 0:
                    print(f"{count} videos synced")

        except Exception as e:

            print(e)

    await message.reply_text(
        f"✅ Synced {count} Videos"
    )
