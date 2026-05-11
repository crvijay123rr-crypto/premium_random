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

    synced = 0
    skipped = 0
    total = 0

    start_msg = await message.reply_text(
        "⚡ Ultra Fast Sync Started..."
    )

    # OLD DATABASE IDS
    old_videos = await get_all_videos()

    old_ids = set()

    for x in old_videos:
        old_ids.add(x["msg_id"])

    # HISTORY SCAN
    async for msg in userbot.get_chat_history(PREMIUM_CHANNEL):

        total += 1

        try:

            if not msg.video:
                continue

            # DUPLICATE SKIP
            if msg.id in old_ids:

                skipped += 1
                continue

            # SAVE VIDEO
            await add_video(
                PREMIUM_CHANNEL,
                msg.id
            )

            synced += 1

            # ADD TO CACHE
            old_ids.add(msg.id)

            # LIVE PROGRESS
            if synced % 100 == 0:

                try:

                    await start_msg.edit_text(
                        f"""
⚡ ULTRA FAST SYNC

✅ Synced : {synced}
⏭ Skipped : {skipped}
📂 Checked : {total}
"""
                    )

                except:
                    pass

        except Exception as e:

            print(f"ERROR : {e}")

    await start_msg.edit_text(
        f"""
✅ ULTRA SYNC COMPLETED

📥 Total Synced : {synced}
⏭ Total Skipped : {skipped}
📂 Total Checked : {total}
"""
    )
