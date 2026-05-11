from pyrogram import filters

from main import app
from admin.admin import admin_filter

from database.stats_db import (
    total_users,
    total_premium_users,
    total_videos,
    total_demo_videos
)

@app.on_message(filters.command("stats") & admin_filter)
async def stats(client, message):

    users = await total_users()
    premium = await total_premium_users()
    videos = await total_videos()
    demo = await total_demo_videos()

    text = f"""
📊 BOT STATS

👥 Users : {users}
👑 Premium : {premium}

🎥 Videos : {videos}
🎁 Demo Videos : {demo}
"""

    await message.reply_text(text)# Stats system
