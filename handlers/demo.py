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

# ANTI SPAM
demo_locks = {}


@app.on_message(filters.command("demo"))
async def demo(client, message):

    user_id = message.from_user.id

    # SPAM PROTECTION
    if user_id in demo_locks:

        return await message.reply_text(
            "⚠️ Please Wait..."
        )

    demo_locks[user_id] = True

    try:

        # ADD USER
        await add_user(user_id)

        # GET USER
        user = await get_user(user_id)

        # DEMO LIMIT
        if user.get("demo_used", 0) >= 1:

            return await message.reply_text(
                """
╔════════════════════╗
      ❌ DEMO FINISHED ❌
╚════════════════════╝

⚠️ Your Free Demo Limit
Has Been Completed

━━━━━━━━━━━━━━━━━━━

💎 Buy Premium For
Unlimited Access

📩 DM FAST :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Unlock Premium Instantly
"""
            )

        # GET DEMO VIDEOS
        demo_videos = await get_demo_videos()

        if not demo_videos:

            return await message.reply_text(
                "❌ No Demo Videos Found"
            )

        # RANDOMIZE
        random.shuffle(demo_videos)

        # SELECT 50
        selected = demo_videos[:50]

        status = await message.reply_text(
            f"⚡ Sending {len(selected)} Demo Videos..."
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

                # FAST SAFE DELAY
                await asyncio.sleep(0.3)

            except FloodWait as e:

                await asyncio.sleep(e.value)

            except Exception as e:

                print(e)

        # INCREASE DEMO
        await increase_demo(user_id)

        # SUCCESS MESSAGE
        await status.edit_text(
            f"""
╔════════════════════╗
      ✅ DEMO SENT ✅
╚════════════════════╝

🎬 Successfully Sent :
{sent_count} Demo Videos

━━━━━━━━━━━━━━━━━━━

⚠️ All Videos Will Be
Deleted Automatically
In 2 Minutes

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

        # DELETE DEMO VIDEOS
        for msg in sent_messages:

            try:
                await msg.delete()

            except:
                pass

        # DELETE STATUS MESSAGE
        try:
            await status.delete()

        except:
            pass

    finally:

        # REMOVE LOCK
        demo_locks.pop(user_id, None)
