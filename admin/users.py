from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.mongo import users


@app.on_message(filters.command("users") & admin_filter)
async def users_list(client, message):

    total = await users.count_documents({})

    all_users = users.find({})

    text = f"""
╔════════════════════╗
       👥 ALL USERS
╚════════════════════╝

📦 Total Users : {total}

━━━━━━━━━━━━━━━━━━━
"""

    count = 0

    async for user in all_users:

        count += 1

        user_id = user.get("user_id")

        name = user.get("name", "Unknown")

        text += f"\n{count}. {name} → `{user_id}`"

    if count == 0:

        text += "\n❌ No Users Found"

    await message.reply_text(text)
