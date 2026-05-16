from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.mongo import users


@app.on_message(filters.command("premiums") & admin_filter)
async def premiums(client, message):

    premium_users = users.find({
        "premium": True
    })

    total = await users.count_documents({
        "premium": True
    })

    text = f"""
╔════════════════════╗
      👑 PREMIUM USERS
╚════════════════════╝

📦 Total Premium Users :
{total}

━━━━━━━━━━━━━━━━━━━
"""

    count = 0

    async for user in premium_users:

        count += 1

        user_id = user.get("user_id")

        text += f"\n{count}. `{user_id}`"

    if count == 0:

        text += "\n❌ No Premium Users Found"

    await message.reply_text(text)
