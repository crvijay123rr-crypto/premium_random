import asyncio
from datetime import datetime

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

from database.mongo import users

from database.videos_db import (
    get_all_videos
)

# ANTI SPAM
user_locks = {}


# AUTO DELETE FUNCTION
async def auto_delete(messages, status_msg):

    await asyncio.sleep(86400)  # 24 HOURS

    for msg in messages:

        try:
            await msg.delete()

        except:
            pass

    try:
        await status_msg.delete()

    except:
        pass


@app.on_message(filters.command("videos"))
async def send_videos(client, message):

    user_id = message.from_user.id

    # SPAM PROTECTION
    if user_id in user_locks:

        return await message.reply_text(
            "⚠️ Please Wait..."
        )

    user_locks[user_id] = True

    try:

        await add_user(user_id)

        # PREMIUM CHECK
        premium = await is_premium(user_id)

        if not premium:

            return await message.reply_text(
                """
╔════════════════════╗
      ❌ ACCESS DENIED ❌
╚════════════════════╝

👑 Premium Membership Required

🔥 Unlock Unlimited Premium Videos
⚡ Daily 100 Videos Access
🛡 Protected Content Enabled

━━━━━━━━━━━━━━━━━━━

💎 Buy Premium First

📩 DM FAST :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Get Instant Premium Access Now
"""
            )

        # GET USER
        user = await get_user(user_id)

        # DAILY LIMIT
        if user.get("used_today", 0) >= DAILY_LIMIT:

            return await message.reply_text(
                """
╔════════════════════╗
      ⚠️ DAILY LIMIT ⚠️
╚════════════════════╝

❌ Your Daily Limit Reached

🎬 Limit :
100 Videos Per Day

⏳ Try Again Tomorrow
"""
            )

        # GET VIDEOS
        all_videos = await get_all_videos()

        if not all_videos:

            return await message.reply_text(
                "❌ No Videos Found"
            )

        today = datetime.utcnow().strftime("%Y-%m-%d")

        last_date = user.get("last_video_date")

        current_index = user.get("video_index", 0)

        # NEXT 100 VIDEOS
        start = current_index
        end = start + 100

        # SAVE NEXT INDEX DAILY
        if last_date != today:

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "last_video_date": today,
                        "video_index": end
                    }
                }
            )

        selected_videos = all_videos[start:end]

        # RESET IF END
        if not selected_videos:

            start = 0
            end = 100

            selected_videos = all_videos[start:end]

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "video_index": end
                    }
                }
            )

        status = await message.reply_text(
            f"⚡ Sending {len(selected_videos)} Premium Videos..."
        )

        sent_messages = []

        sent_count = 0

        # SEND VIDEOS
        for video in selected_videos:

            try:

                sent = await app.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=video["channel"],
                    message_id=video["msg_id"],
                    protect_content=True
                )

                sent_messages.append(sent)

                sent_count += 1

                # SAFE DELAY
                await asyncio.sleep(0.3)

            except FloodWait as e:

                await asyncio.sleep(e.value)

            except Exception as e:

                print(e)

        # INCREASE DAILY LIMIT
        await increase_limit(user_id)

        # SAVE TOTAL RECEIVED
        await users.update_one(
            {"user_id": user_id},
            {
                "$inc": {
                    "total_received": sent_count
                }
            }
        )

        # SUCCESS MESSAGE
        await status.edit_text(
            f"""
╔════════════════════╗
      ✅ VIDEOS SENT ✅
╚════════════════════╝

🎬 Successfully Sent :
{sent_count} Premium Videos

📦 Total Received :
{user.get('total_received', 0) + sent_count}

⚠️ Videos Will Auto Delete
After 24 Hours

🔥 Enjoy Premium Access
"""
        )

        # RUN AUTO DELETE IN BACKGROUND
        asyncio.create_task(
            auto_delete(sent_messages, status)
        )

    finally:

        # REMOVE LOCK
        user_locks.pop(user_id, None)import asyncio
from datetime import datetime

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

from database.mongo import users

from database.videos_db import (
    get_all_videos
)

# ANTI SPAM
user_locks = {}


# AUTO DELETE FUNCTION
async def auto_delete(messages, status_msg):

    await asyncio.sleep(86400)  # 24 HOURS

    for msg in messages:

        try:
            await msg.delete()

        except:
            pass

    try:
        await status_msg.delete()

    except:
        pass


@app.on_message(filters.command("videos"))
async def send_videos(client, message):

    user_id = message.from_user.id

    # SPAM PROTECTION
    if user_id in user_locks:

        return await message.reply_text(
            "⚠️ Please Wait..."
        )

    user_locks[user_id] = True

    try:

        await add_user(user_id)

        # PREMIUM CHECK
        premium = await is_premium(user_id)

        if not premium:

            return await message.reply_text(
                """
╔════════════════════╗
      ❌ ACCESS DENIED ❌
╚════════════════════╝

👑 Premium Membership Required

🔥 Unlock Unlimited Premium Videos
⚡ Daily 100 Videos Access
🛡 Protected Content Enabled

━━━━━━━━━━━━━━━━━━━

💎 Buy Premium First

📩 DM FAST :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Get Instant Premium Access Now
"""
            )

        # GET USER
        user = await get_user(user_id)

        # DAILY LIMIT
        if user.get("used_today", 0) >= DAILY_LIMIT:

            return await message.reply_text(
                """
╔════════════════════╗
      ⚠️ DAILY LIMIT ⚠️
╚════════════════════╝

❌ Your Daily Limit Reached

🎬 Limit :
100 Videos Per Day

⏳ Try Again Tomorrow
"""
            )

        # GET VIDEOS
        all_videos = await get_all_videos()

        if not all_videos:

            return await message.reply_text(
                "❌ No Videos Found"
            )

        today = datetime.utcnow().strftime("%Y-%m-%d")

        last_date = user.get("last_video_date")

        current_index = user.get("video_index", 0)

        # NEXT 100 VIDEOS
        start = current_index
        end = start + 100

        # SAVE NEXT INDEX DAILY
        if last_date != today:

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "last_video_date": today,
                        "video_index": end
                    }
                }
            )

        selected_videos = all_videos[start:end]

        # RESET IF END
        if not selected_videos:

            start = 0
            end = 100

            selected_videos = all_videos[start:end]

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "video_index": end
                    }
                }
            )

        status = await message.reply_text(
            f"⚡ Sending {len(selected_videos)} Premium Videos..."
        )

        sent_messages = []

        sent_count = 0

        # SEND VIDEOS
        for video in selected_videos:

            try:

                sent = await app.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=video["channel"],
                    message_id=video["msg_id"],
                    protect_content=True
                )

                sent_messages.append(sent)

                sent_count += 1

                # SAFE DELAY
                await asyncio.sleep(0.3)

            except FloodWait as e:

                await asyncio.sleep(e.value)

            except Exception as e:

                print(e)

        # INCREASE DAILY LIMIT
        await increase_limit(user_id)

        # SAVE TOTAL RECEIVED
        await users.update_one(
            {"user_id": user_id},
            {
                "$inc": {
                    "total_received": sent_count
                }
            }
        )

        # SUCCESS MESSAGE
        await status.edit_text(
            f"""
╔════════════════════╗
      ✅ VIDEOS SENT ✅
╚════════════════════╝

🎬 Successfully Sent :
{sent_count} Premium Videos

📦 Total Received :
{user.get('total_received', 0) + sent_count}

⚠️ Videos Will Auto Delete
After 24 Hours

🔥 Enjoy Premium Access
"""
        )

        # RUN AUTO DELETE IN BACKGROUND
        asyncio.create_task(
            auto_delete(sent_messages, status)
        )

    finally:

        # REMOVE LOCK
        user_locks.pop(user_id, None)                }
            )

        status = await message.reply_text(
            f"⚡ Sending {len(selected_videos)} Premium Videos..."
        )

        sent_messages = []

        sent_count = 0

        # SEND VIDEOS
        for video in selected_videos:

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

        # INCREASE LIMIT
        await increase_limit(user_id)

        # SAVE TOTAL RECEIVED
        await users.update_one(
            {"user_id": user_id},
            {
                "$inc": {
                    "total_received": sent_count
                }
            }
        )

        # SUCCESS MESSAGE
        await status.edit_text(
            f"""
╔════════════════════╗
      ✅ VIDEOS SENT ✅
╚════════════════════╝

🎬 Successfully Sent :
{sent_count} Premium Videos

📦 Total Received :
{user.get('total_received', 0) + sent_count}

⚠️ Videos Will Auto Delete
After 24 Hours

🔥 Enjoy Premium Access
"""
        )

        # AUTO DELETE AFTER 24 HOURS
        await asyncio.sleep(86400)

        for msg in sent_messages:

            try:
                await msg.delete()

            except:
                pass

        try:
            await status.delete()

        except:
            pass

    finally:

        # REMOVE LOCK
        user_locks.pop(user_id, None)
