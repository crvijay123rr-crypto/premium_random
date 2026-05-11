from pyrogram import filters

from bot import app, userbot
from config import DEMO_CHANNEL

from admin.admin import admin_filter

from database.videos_db import add_demo


@app.on_message(filters.command("syncdemo") & admin_filter)
async def sync_demo(client, message):

    success = 0
    failed = 0
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

            # ONLY VIDEOS
            if msg.video or msg.document:

                await add_demo(
                    DEMO_CHANNEL,
                    msg.id
                )

                success += 1

            else:
                failed += 1

        except Exception as e:

            failed += 1

            print(f"SYNC ERROR : {e}")

        # UPDATE PROGRESS EVERY 10 MSGS
        if total % 10 == 0:

            await status.edit_text(
                f"""
╔════════════════════╗
      🔄 DEMO SYNC 🔄
╚════════════════════╝

📦 Checked :
{total}

✅ Success :
{success}

❌ Failed :
{failed}

⏳ Sync Running...
"""
            )

    # FINAL MESSAGE
    await status.edit_text(
        f"""
╔════════════════════╗
      ✅ DEMO SYNCED ✅
╚════════════════════╝

📦 Total Checked :
{total}

✅ Successfully Synced :
{success}

❌ Failed :
{failed}

🔥 Demo Database Updated
"""
    )
