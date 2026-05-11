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


@app.on_message(filters.command("videos"))
async def send_videos(client, message):

    user_id = message.from_user.id

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
            "❌ Daily Limit Reached"
        )

    all_videos = await get_all_videos()

    if not all_videos:

        return await message.reply_text(
            "❌ No Videos Found"
        )

    today = datetime.utcnow().strftime("%Y-%m-%d")

    last_date = user.get("last_video_date")

    current_index = user.get("video_index", 0)

    # SAME DAY = SAME VIDEOS
    if last_date == today:

        start = current_index
        end = start + 100

    else:

        # NEXT DAY START FROM NEXT 100
        start = current_index
        end = start + 100

        # SAVE NEXT POSITION
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

    # RESET IF END REACHED
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

    await message.reply_text(
        f"🎬 Sending {len(selected_videos)} Premium Videos..."
    )

    sent_messages = []

    sent_count = 0

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

            await asyncio.sleep(1)

        except FloodWait as e:

            await asyncio.sleep(e.value)

        except Exception as e:

            print(e)

    await increase_limit(user_id)

    warning = await message.reply_text(
        "⚠️ Premium videos will auto delete after 24 hours."
    )

    # DELETE AFTER 24 HOURS
    await asyncio.sleep(86400)

    for msg in sent_messages:

        try:
            await msg.delete()

        except:
            pass

    try:
        await warning.delete()

    except:
        pass
