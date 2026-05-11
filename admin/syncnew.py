from pyrogram import filters

from bot import app, userbot
from config import PREMIUM_CHANNEL

from admin.admin import admin_filter

from database.videos_db import add_video
from database.sync_db import (
    get_last_msg,
    save_last_msg
)


@app.on_message(filters.command("syncnew") & admin_filter)
async def sync_new(client, message):

    synced = 0
    failed = 0
    checked = 0

    start_msg = await message.reply_text(
        """
╔════════════════════╗
     ⚡ NEW SYNC STARTED ⚡
╚════════════════════╝

🔄 Checking New Videos...
"""
    )

    try:

        # LAST SAVED MESSAGE ID
        last_msg_id = await get_last_msg()

        latest_id = last_msg_id

        # SCAN HISTORY
        async for msg in userbot.get_chat_history(PREMIUM_CHANNEL):

            checked += 1

            try:

                # STOP OLD MESSAGES
                if msg.id <= last_msg_id:
                    break

                # ONLY VIDEOS
                if not msg.video:
                    continue

                # SAVE VIDEO
                await add_video(
                    PREMIUM_CHANNEL,
                    msg.id
                )

                synced += 1

                print(f"✅ Synced : {msg.id}")

                # SAVE LATEST ID
                if msg.id > latest_id:
                    latest_id = msg.id

                # LIVE UPDATE
                if synced % 20 == 0:

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
{checked}

✅ Synced :
{synced}

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

        # SAVE LAST MESSAGE
        await save_last_msg(latest_id)

        # FINAL MESSAGE
        await start_msg.edit_text(
            f"""
╔════════════════════╗
    ✅ NEW SYNC COMPLETED ✅
╚════════════════════╝

📂 Total Checked :
{checked}

✅ Total Synced :
{synced}

❌ Total Failed :
{failed}

🆕 Latest Videos Added Successfully
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
