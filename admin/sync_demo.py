import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait

from bot import app, userbot
from config import DEMO_CHANNEL

from admin.admin import admin_filter

from database.videos_db import add_demo


@app.on_message(filters.command("syncdemo") & admin_filter)
async def sync_demo(client, message):

    success = 0
    failed = 0
    skipped = 0
    total = 0

    status = await message.reply_text(
        """
╔════════════════════╗
      🔄 DEMO SYNC 🔄
╚════════════════════╝

⏳ Starting Sync...
"""
    )

    async for msg in userbot.get_chat_history(DEMO_CHANNEL):

        total += 1

        try:

            # EMPTY MESSAGE
            if msg.empty:
                skipped += 1
                continue

            # ONLY VIDEO FILES
            if not (
                msg.video
                or msg.document
                or msg.animation
            ):
                skipped += 1
                continue

            # ADD DEMO
            added = await add_demo(
                DEMO_CHANNEL,
                msg.id
            )

            if added:
                success += 1
            else:
                skipped += 1

            # ANTI FLOOD
            await asyncio.sleep(1)

        except FloodWait as e:

            print(f"FLOODWAIT : {e.value}")

            await asyncio.sleep(e.value)

        except Exception as e:

            failed += 1

            print(f"SYNC ERROR : {e}")

        # UPDATE EVERY 10 MSGS
        if total % 10 == 0:

            await status.edit_text(
                f"""
╔════════════════════╗
      🔄 DEMO SYNC 🔄
╚════════════════════╝

📦 Checked : {total}

✅ Success : {success}

⏭️ Skipped : {skipped}

❌ Failed : {failed}

⏳ Sync Running...
"""
            )

    # FINAL MESSAGE
    await status.edit_text(
        f"""
╔════════════════════╗
      ✅ DEMO SYNCED ✅
╚════════════════════╝

📦 Total Checked : {total}

✅ Synced : {success}

⏭️ Skipped : {skipped}

❌ Failed : {failed}

🔥 Demo Database Updated
"""
    )
