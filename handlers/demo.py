import asyncio
import random

from pyrogram import filters

from bot import app

from database.users_db import (
    get_user,
    increase_demo
)

from database.videos_db import (
    get_demo_videos
)

@app.on_message(filters.command("demo"))
async def demo(client, message):

    user = await get_user(message.from_user.id)

    if user["demo_used"] >= 50:
        return await message.reply_text(
            "❌ Demo Limit Finished"
        )

    demo_videos = await get_demo_videos()

    if not demo_videos:
        return await message.reply_text(
            "❌ No Demo Videos"
        )

    video = random.choice(demo_videos)

    sent = await app.copy_message(
        chat_id=message.chat.id,
        from_chat_id=video["channel"],
        message_id=video["msg_id"],
        protect_content=True
    )

    await increase_demo(message.from_user.id)

    await asyncio.sleep(120)

    try:
        await sent.delete()
    except:
        pass# Demo handler
