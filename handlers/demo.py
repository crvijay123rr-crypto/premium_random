import asyncio
import random

from pyrogram import filters
from pyrogram.errors import FloodWait

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

    # GET USER
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

    # RANDOMIZE VIDEOS
    random.shuffle(demo_videos)

    # SELECT 50 VIDEOS
    selected = demo_videos[:50]

    await message.reply_text(
        f"🎬 Sending {len(selected)} Demo Videos..."
    )

    sent_messages = []

    sent_count = 0

    # SEND VIDEOS
    for video in selected:

        try:

            sent = await app.copy_message(
                chat_id=message.chat.id,
                from_chat_id=video["channel"],
                message_id=video["msg_id"],
                protect_content=True
            )

            sent_messages.append(sent)

            sent_count += 1

            # SMALL DELAY
            await asyncio.sleep(1)

        except FloodWait as e:

            print(f"FloodWait: {e.value}")

            await asyncio.sleep(e.value)

        except Exception as e:

            print(e)

    # INCREASE DEMO LIMIT
    await increase_demo(user_id)

    # SUCCESS MESSAGE
await message.reply_text(
    f"✅ Sent {sent_count} Demo Videos"
)

# WARNING MESSAGE
warning_msg = await message.reply_text(
    """
╔════════════════════╗
       ⚠️ DEMO NOTICE ⚠️
╚════════════════════╝

🎥 These Were Only Demo Videos

🗑 All Demo Videos Will Be
Deleted Automatically In 2 Minutes

━━━━━━━━━━━━━━━━━━━

💎 Buy Premium For
Unlimited Full Access

📩 DM FAST :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Unlock Premium Instantly
"""
)

# WAIT 2 MINUTES
await asyncio.sleep(120)

    # DELETE ALL DEMO VIDEOS
    for msg in sent_messages:

        try:
            await msg.delete()

        except Exception as e:
            print(e)

    # DELETE WARNING MESSAGE
    try:
        await warning_msg.delete()

    except:
        pass
