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
    failed = 0
    total = 0

    start_msg = await message.reply_text(
        """
╔════════════════════╗
      ⚡ SYNC STARTED ⚡
╚════════════════════╝

🔄 Scanning Premium Channel...
"""
    )

    try:

        # LOAD CHAT
        chat = await userbot.get_chat(PREMIUM_CHANNEL)

        # OLD DATABASE IDS
        old_videos = await get_all_videos()

        old_ids = set()

        for x in old_videos:
            old_ids.add(x["msg_id"])

        # HISTORY SCAN
        async for msg in userbot.get_chat_history(chat.id):

            total += 1

            try:

                # ONLY VIDEO
                if not msg.video:
                    continue

                # DUPLICATE SKIP
                if msg.id in old_ids:

                    skipped += 1
                    continue

                # SAVE VIDEO
                await add_video(
                    chat.id,
                    msg.id
                )

                synced += 1

                # CACHE UPDATE
                old_ids.add(msg.id)

                print(f"✅ Synced : {msg.id}")

                # LIVE PROGRESS UPDATE
                if total % 50 == 0:

                    progress = (
                        "▓" * min(synced // 10, 10)
                    ).ljust(10, "░")

                    try:

                        await start_msg.edit_text(
                            f"""
╔════════════════════╗
      ⚡ SYNC RUNNING ⚡
╚════════════════════╝

📂 Checked :
{total}

✅ Synced :
{synced}

⏭ Skipped :
{skipped}

❌ Failed :
{failed}

[{progress}]
"""
                        )

                    except:
                        pass

            except Exception as e:

                failed += 1

                print(f"❌ ERROR : {e}")

        # FINAL SUCCESS
        await start_msg.edit_text(
            f"""
╔════════════════════╗
     ✅ SYNC COMPLETED ✅
╚════════════════════╝

📂 Total Checked :
{total}

✅ Total Synced :
{synced}

⏭ Total Skipped :
{skipped}

❌ Total Failed :
{failed}

🚀 Premium Database Updated
"""
        )

    except Exception as e:

        await start_msg.edit_text(
            f"""
╔════════════════════╗
       ❌ SYNC FAILED ❌
╚════════════════════╝

⚠️ Error :
{e}
"""
        )
