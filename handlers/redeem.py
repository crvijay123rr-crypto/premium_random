from pyrogram import filters

from bot import app

@app.on_message(filters.command("redeem"))
async def redeem(client, message):

    text = """
🎁 REDEEM SYSTEM

Feature Coming Soon
"""

    await message.reply_text(text)# Redeem handler
