from pyrogram import filters

from bot import app

@app.on_message(filters.command("support"))
async def support(client, message):

    text = """
☎ SUPPORT

👤 Admin :
@Contact_45bot
"""

    await message.reply_text(text)# Support handler
