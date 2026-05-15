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


# =========================
# RESET DEMO COMMAND
# =========================
@app.on_message(filters.command("resetdemo"))
async def reset_demo_command(client, message):

    reset_msg = await message.reply_text(
        """
╔══════════════════════╗
       ♻️ RESETTING ♻️
╚══════════════════════╝

⚡ Resetting All Users
Free Demo Access...

📡 Sending Notifications...
"""
    )

    # RESET ALL USERS
    await users.update_many(
        {},
        {
            "$set": {
                "demo_used": 0,
                "last_demo_date": None
            }
        }
    )

    # GET ALL USERS
    all_users = users.find({})

    sent = 0
    failed = 0

    # BROADCAST MESSAGE
    async for user in all_users:

        try:

            await app.send_message(
                chat_id=user["user_id"],
                text="""
╔══════════════════════╗
      🎉 DEMO RESET 🎉
╚══════════════════════╝

🔥 Your Free Demo
Has Been Reset Successfully

🎬 Use /demo Now
And Enjoy Fresh Content

⚡ Hurry Before
Daily Limit Ends
"""
            )

            sent += 1

            await asyncio.sleep(0.1)

        except:

            failed += 1

    # FINAL STATUS
    await reset_msg.edit_text(
        f"""
╔══════════════════════╗
      ✅ RESET DONE ✅
╚══════════════════════╝

🎬 All Demo Users Reset
Successfully

📢 Notifications Sent :
{sent}

❌ Failed Users :
{failed}

🚀 Everyone Can Use
/demo Again
"""
    )
