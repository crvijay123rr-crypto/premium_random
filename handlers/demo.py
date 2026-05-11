import asyncio
import random

from pyrogram import filters

from bot import app

from database.users_db import (
    get_user,
    increase_demo,
    add_user
)

from database.videos_db import (
    get_demo_videos
)


@app.on_message(filters.command("demo"))
async def demo(client, message):

    user_id = message.from_user.id

    # ADD USER
    await add_user(user_id)

    user = await get_user(user_id)

    # DEMO LIMIT
    if user.get("demo_used", 0) >= 1:

        return await message.reply_text(
            "❌ Demo Limit Finished"
        )

    # GET DEMO VIDEOS
    demo_videos = await get_demo_videos()

    if not demo_videos:

        return await message.reply_text(
            "❌ No Demo Videos"
        )

    # RANDOMIZE
    random.shuffle(demo_videos)

    selected = demo_videos[:50]

    await message.reply_text(
        f"🎬 Sending {len(selected)} Demo Videos..."
    )

    sent_count = 0

    for video in selected:

        try:

            await app.copy_message(
                chat_id=message.chat.id,
                from_chat_id=video["channel"],
                message_id=video["msg_id"],
                protect_content=True
            )

            sent_count += 1

            await asyncio.sleep(1)

        except Exception as e:

            print(e)

    # INCREASE DEMO LIMIT
    await increase_demo(user_id)

    await message.reply_text(
        f"✅ Sent {sent_count} Demo Videos"
    )
