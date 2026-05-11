from pyrogram import filters

from main import app

@app.on_message(filters.command("refer"))
async def refer(client, message):

    link = f"https://t.me/{client.me.username}?start={message.from_user.id}"

    text = f"""
👥 REFERRAL PROGRAM

Invite Friends & Earn Premium

🔗 Your Link:
{link}
"""

    await message.reply_text(text)# Referral handler
