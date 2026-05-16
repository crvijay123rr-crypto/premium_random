# =========================
# DEMO COMMAND
# =========================

import asyncio
import random
from datetime import datetime

from pyrogram import filters
from pyrogram.errors import FloodWait

from bot import app

from database.users_db import (
    get_user,
    add_user
)

from database.mongo import users

from database.videos_db import (
    get_demo_videos
)

# ANTI SPAM
demo_locks = {}


@app.on_message(filters.command("demo"))
async def demo(client, message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name

    # SPAM PROTECTION
    if user_id in demo_locks:

        return await message.reply_text(
            "⚠️ Please Wait..."
        )

    demo_locks[user_id] = True

    try:

        # ADD USER
        await add_user(message.from_user)

        # SAVE NAME
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "name": first_name
                }
            }
        )

        # GET USER
        user = await get_user(user_id)

        today = datetime.utcnow().strftime("%Y-%m-%d")

        demo_used = user.get("demo_used", 0)

        last_demo_date = user.get("last_demo_date")

        # RESET DAILY
        if last_demo_date != today:

            demo_used = 0

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "demo_used": 0,
                        "last_demo_date": today
                    }
                }
            )

        # CHECK LIMIT
        if demo_used >= 1:

            return await message.reply_text(
                """
╔════════════════════╗
      ❌ DEMO USED ❌
╚════════════════════╝

⚠️ You Already Used
Today's Free Demo

⏳ Try Again Tomorrow
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

                await asyncio.sleep(0.3)

            except FloodWait as e:

                await asyncio.sleep(e.value)

            except Exception as e:

                print(f"DEMO SEND ERROR : {e}")

        # SAVE DEMO USED
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "demo_used": 1,
                    "last_demo_date": today
                }
            }
        )

        # SUCCESS MESSAGE
        await status.edit_text(
            f"""
╔════════════════════╗
      ✅ DEMO SENT ✅
╚════════════════════╝

🎬 Successfully Sent :
{sent_count} Demo Videos

⚠️ Videos Will Auto Delete
In 2 Minutes

🚀 Come Back Tomorrow
For Next Free Demo
"""
        )

        # PIN SUCCESS MESSAGE
        try:

            await status.pin(
                disable_notification=True
            )

        except:
            pass

        # AUTO DELETE AFTER 2 MINUTES
        await asyncio.sleep(120)

        # DELETE VIDEOS
        for msg in sent_messages:

            try:
                await msg.delete()

            except:
                pass

        # UNPIN MESSAGE
        try:

            await status.unpin()

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
