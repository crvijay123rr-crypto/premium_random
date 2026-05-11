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

    await message.reply_text(
        "🔄 Syncing New Videos..."
    )

    last_msg_id = await get_last_msg()

    count = 0
    latest_id = last_msg_id

    async for msg in userbot.get_chat_history(PREMIUM_CHANNEL):

        try:

            # STOP OLD MESSAGES
            if msg.id <= last_msg_id:
                break

            if msg.video:

                await add_video(
                    PREMIUM_CHANNEL,
                    msg.id
                )

                count += 1

                # SAVE LATEST ID
                if msg.id > latest_id:
                    latest_id = msg.id

        except Exception as e:

            print(e)

    # SAVE LAST MESSAGE
    await save_last_msg(latest_id)

    await message.reply_text(
        f"✅ Synced {count} New Videos"
    )
