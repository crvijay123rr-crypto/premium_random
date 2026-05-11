import asyncio
import random

from pyrogram import filters
from pyrogram.errors import FloodWait

from bot import app
from config import DAILY_LIMIT

from database.users_db import (
    get_user,
    increase_limit,
    is_premium,
    add_user
)

from database.videos_db import (
    get_all_videos
)


@app.on_message(filters.command("videos"))
async def send_videos(client, message):

    user_id = message.from_user.id

    # ADD USER
    await add_user(user_id)

    # PREMIUM CHECK
    premium = await is_premium(user_id)

    if not premium:

        return await message.reply_text(
            "❌ Buy Premium First"
        )

    # GET USER
    user = await get_user(user_id)

    # DAILY LIMIT CHECK
    if user.get("used_today", 0) >= DAILY_LIMIT:

        return await message.reply_text(
            "❌ Daily Limit Reached"
        )

    # GET ALL VIDEOS
    all_videos = await get_all_videos()

    if not all_videos:

        return await message.reply_text(
            "❌ No Videos Found"
        )

    # RANDOMIZE VIDEOS
    random.shuffle(all_videos)

    # SELECT 100 VIDEOS
    selected_videos = all_videos[:100]

    await message.reply_text(
        f"🎬 Sending {len(selected_videos)} Premium Videos..."
    )

    sent_count = 0

    # SEND VIDEOS
    for video in selected_videos:

        try:

            await app.copy_message(
                chat_id=message.chat.id,
                from_chat_id=video["channel"],
                message_id=video["msg_id"],
                protect_content=True
            )

            sent_count += 1

            # SMALL DELAY
            await asyncio.sleep(1)

        except FloodWait as e:

            print(f"FloodWait: {e.value}")

            await asyncio.sleep(e.value)

        except Exception as e:

            print(e)

    # INCREASE LIMIT
    await increase_limit(user_id)

    # DONE MESSAGE
    await message.reply_text(
        f"✅ Successfully Sent {sent_count} Videos"
    )
