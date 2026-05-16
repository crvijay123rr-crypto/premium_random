import asyncio
from datetime import datetime

from pyrogram import filters
from pyrogram.errors import FloodWait

from bot import app, userbot
from config import DAILY_LIMIT

from database.users_db import (
    get_user,
    increase_limit,
    is_premium,
    add_user
)

from database.mongo import users
from database.videos_db import get_all_videos


# =========================
# ANTI SPAM
# =========================
user_locks = {}


# =========================
# AUTO DELETE FUNCTION
# =========================
async def auto_delete(messages, status_msg):

    await asyncio.sleep(86400)

    for msg in messages:

        try:
            await msg.delete()

        except:
            pass

    try:
        await status_msg.delete()

    except:
        pass


# =========================
# VIDEOS COMMAND
# =========================
@app.on_message(filters.command("videos"))
async def send_videos(client, message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name

    # =========================
    # SPAM PROTECTION
    # =========================
    if user_id in user_locks:

        return await message.reply_text(
            "⚠️ Please Wait..."
        )

    user_locks[user_id] = True

    try:

        # =========================
        # ADD USER
        # =========================
        await add_user(message.from_user)

        # =========================
        # SAVE USER NAME
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "name": first_name
                }
            }
        )

        # =========================
        # PREMIUM CHECK
        # =========================
        premium = await is_premium(user_id)

        print(f"USER ID : {user_id}")
        print(f"PREMIUM : {premium}")

        if not premium:

            return await message.reply_text(
                """
╔════════════════════╗
      ❌ ACCESS DENIED ❌
╚════════════════════╝

👑 Premium Membership Required

🔥 Unlock Unlimited Premium Videos
⚡ 100 Videos Per Click
🎬 Daily Access : 200 Videos
🛡 Protected Content Enabled

━━━━━━━━━━━━━━━━━━━

💎 Buy Premium First

📩 DM FAST :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Get Instant Premium Access Now
"""
            )

        # =========================
        # GET USER
        # =========================
        user = await get_user(user_id)

        if not user:

            return await message.reply_text(
                "❌ User Data Not Found"
            )

        # =========================
        # DAILY LIMIT RESET
        # =========================
        today = datetime.utcnow().strftime("%Y-%m-%d")

        last_limit_date = user.get("last_limit_date")

        if last_limit_date != today:

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "used_today": 0,
                        "last_limit_date": today
                    }
                }
            )

            user["used_today"] = 0

        # =========================
        # DAILY LIMIT CHECK
        # =========================
        if user.get("used_today", 0) >= DAILY_LIMIT:

            return await message.reply_text(
                f"""
╔════════════════════╗
      ⚠️ DAILY LIMIT ⚠️
╚════════════════════╝

❌ Your Daily Limit Reached

🎬 Limit :
200 Videos Per Day

⏳ Try Again Tomorrow
"""
            )

        # =========================
        # GET VIDEOS
        # =========================
        all_videos = await get_all_videos()

        if not all_videos:

            return await message.reply_text(
                "❌ No Videos Found"
            )

        # =========================
        # VIDEO INDEX SYSTEM
        # =========================
        current_index = user.get("video_index", 0)

        start = current_index
        end = start + 100

        selected_videos = all_videos[start:end]

        # RESET IF VIDEOS END
        if not selected_videos:

            start = 0
            end = 100

            selected_videos = all_videos[start:end]

        # =========================
        # SAVE NEXT INDEX
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "video_index": end
                }
            }
        )

        # =========================
        # STATUS MESSAGE
        # =========================
        status = await message.reply_text(
            f"⚡ Sending {len(selected_videos)} Premium Videos..."
        )

        sent_messages = []
        sent_count = 0

        # =========================
        # SEND VIDEOS
        # =========================
        for video in selected_videos:

            try:

                # TRY USERBOT FIRST
                try:

                    sent = await userbot.copy_message(
                        chat_id=message.chat.id,
                        from_chat_id=video["channel"],
                        message_id=video["msg_id"]
                    )

                # FALLBACK TO BOT
                except:

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

                print(f"VIDEO SEND ERROR : {e}")

        # =========================
        # INCREASE LIMIT
        # =========================
        await increase_limit(user_id)

        # =========================
        # SAVE TOTAL RECEIVED
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$inc": {
                    "total_received": sent_count
                }
            }
        )

        # =========================
        # SUCCESS MESSAGE
        # =========================
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

        # =========================
        # AUTO DELETE TASK
        # =========================
        asyncio.create_task(
            auto_delete(
                sent_messages,
                status
            )
        )

    finally:

        # =========================
        # REMOVE LOCK
        # =========================
        user_locks.pop(user_id, None)
💎 Buy Premium First

📩 DM FAST :
@Contact_45bot

━━━━━━━━━━━━━━━━━━━

🚀 Get Instant Premium Access Now
"""
            )

        # =========================
        # GET USER
        # =========================
        user = await get_user(user_id)

        if not user:

            return await message.reply_text(
                "❌ User Data Not Found"
            )

        # =========================
        # DAILY LIMIT RESET
        # =========================
        today = datetime.utcnow().strftime("%Y-%m-%d")

        last_limit_date = user.get("last_limit_date")

        if last_limit_date != today:

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "used_today": 0,
                        "last_limit_date": today
                    }
                }
            )

            user["used_today"] = 0

        # =========================
        # DAILY LIMIT CHECK
        # =========================
        if user.get("used_today", 0) >= DAILY_LIMIT:

            return await message.reply_text(
                f"""
╔════════════════════╗
      ⚠️ DAILY LIMIT ⚠️
╚════════════════════╝

❌ Your Daily Limit Reached

🎬 Limit :
200 Videos Per Day

⏳ Try Again Tomorrow
"""
            )

        # =========================
        # GET VIDEOS
        # =========================
        all_videos = await get_all_videos()

        if not all_videos:

            return await message.reply_text(
                "❌ No Videos Found"
            )

        # =========================
        # VIDEO INDEX SYSTEM
        # =========================
        current_index = user.get("video_index", 0)

        start = current_index
        end = start + 100

        selected_videos = all_videos[start:end]

        # RESET IF VIDEOS END
        if not selected_videos:

            start = 0
            end = 100

            selected_videos = all_videos[start:end]

        # =========================
        # SAVE NEXT INDEX
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "video_index": end
                }
            }
        )

        # =========================
        # STATUS MESSAGE
        # =========================
        status = await message.reply_text(
            f"⚡ Sending {len(selected_videos)} Premium Videos..."
        )

        sent_messages = []
        sent_count = 0

        # =========================
        # SEND VIDEOS
        # =========================
        for video in selected_videos:

            try:

                # TRY USERBOT FIRST
                try:

                    sent = await userbot.copy_message(
                        chat_id=message.chat.id,
                        from_chat_id=video["channel"],
                        message_id=video["msg_id"]
                    )

                # FALLBACK TO BOT
                except:

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

                print(f"VIDEO SEND ERROR : {e}")

        # =========================
        # INCREASE LIMIT
        # =========================
        await increase_limit(user_id)

        # =========================
        # SAVE TOTAL RECEIVED
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$inc": {
                    "total_received": sent_count
                }
            }
        )

        # =========================
        # SUCCESS MESSAGE
        # =========================
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

        # =========================
        # AUTO DELETE TASK
        # =========================
        asyncio.create_task(
            auto_delete(
                sent_messages,
                status
            )
        )

    finally:

        # =========================
        # REMOVE LOCK
        # =========================
        user_locks.pop(user_id, None)        # GET USER
        # =========================
        user = await get_user(user_id)

        if not user:

            return await message.reply_text(
                "❌ User Data Not Found"
            )

        # =========================
        # DAILY LIMIT RESET
        # =========================
        today = datetime.utcnow().strftime("%Y-%m-%d")

        last_limit_date = user.get("last_limit_date")

        if last_limit_date != today:

            await users.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "used_today": 0,
                        "last_limit_date": today
                    }
                }
            )

            user["used_today"] = 0

        # =========================
        # DAILY LIMIT CHECK
        # =========================
        if user.get("used_today", 0) >= DAILY_LIMIT:

            return await message.reply_text(
                f"""
╔════════════════════╗
      ⚠️ DAILY LIMIT ⚠️
╚════════════════════╝

❌ Your Daily Limit Reached

🎬 Limit :
200 Videos Per Day

⏳ Try Again Tomorrow
"""
            )

        # =========================
        # GET VIDEOS
        # =========================
        all_videos = await get_all_videos()

        if not all_videos:

            return await message.reply_text(
                "❌ No Videos Found"
            )

        # =========================
        # VIDEO INDEX SYSTEM
        # =========================
        current_index = user.get("video_index", 0)

        start = current_index
        end = start + 100

        selected_videos = all_videos[start:end]

        # RESET IF VIDEOS END
        if not selected_videos:

            start = 0
            end = 100

            selected_videos = all_videos[start:end]

        # =========================
        # SAVE NEXT INDEX
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "video_index": end
                }
            }
        )

        # =========================
        # STATUS MESSAGE
        # =========================
        status = await message.reply_text(
            f"⚡ Sending {len(selected_videos)} Premium Videos..."
        )

        sent_messages = []
        sent_count = 0

        # =========================
        # SEND VIDEOS
        # =========================
        for video in selected_videos:

            try:

                print(video)

                # TRY USERBOT FIRST
                try:

                    sent = await userbot.copy_message(
                        chat_id=message.chat.id,
                        from_chat_id=video["channel"],
                        message_id=video["msg_id"]
                    )

                # FALLBACK TO NORMAL BOT
                except Exception as userbot_error:

                    print(f"USERBOT ERROR : {userbot_error}")

                    sent = await app.copy_message(
                        chat_id=message.chat.id,
                        from_chat_id=video["channel"],
                        message_id=video["msg_id"]
                    )

                sent_messages.append(sent)

                sent_count += 1

                await asyncio.sleep(0.3)

            except FloodWait as e:

                await asyncio.sleep(e.value)

            except Exception as e:

                print(f"VIDEO SEND ERROR : {e}")

        # =========================
        # INCREASE LIMIT
        # =========================
        await increase_limit(user_id)

        # =========================
        # SAVE TOTAL RECEIVED
        # =========================
        await users.update_one(
            {"user_id": user_id},
            {
                "$inc": {
                    "total_received": sent_count
                }
            }
        )

        # =========================
        # SUCCESS MESSAGE
        # =========================
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

        # =========================
        # AUTO DELETE TASK
        # =========================
        asyncio.create_task(
            auto_delete(
                sent_messages,
                status
            )
        )

    finally:

        # =========================
        # REMOVE LOCK
        # =========================
        user_locks.pop(user_id, None)
