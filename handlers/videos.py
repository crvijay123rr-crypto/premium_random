import random

from pyrogram import filters

from bot import app
from config import DAILY_LIMIT

from database.users_db import (
    get_user,
    increase_limit,
    is_premium
)

from database.videos_db import (
    get_all_videos
)

@app.on_message(filters.command("videos"))
async def send_videos(client, message):

    premium = await is_premium(message.from_user.id)

    if not premium:
        return await message.reply_text(
            "❌ Buy Premium First"
        )

    user = await get_user(message.from_user.id)

    if user["used_today"] >= DAILY_LIMIT:
        return await message.reply_text(
            "❌ Daily Limit Reached"
        )

    all_videos = await get_all_videos()

    if not all_videos:
        return await message.reply_text(
            "❌ No Videos Found"
        )

    video = random.choice(all_videos)

    caption = f"""
╔════════════════╗
   👑 PREMIUM HUB 👑
╚════════════════╝

👤 User : {message.from_user.mention}
🆔 ID : {message.from_user.id}

⚡ Protected Content
"""

    await app.copy_message(
        chat_id=message.chat.id,
        from_chat_id=video["channel"],
        message_id=video["msg_id"],
        protect_content=True
    )

    await increase_limit(message.from_user.id)# Video sender handler
