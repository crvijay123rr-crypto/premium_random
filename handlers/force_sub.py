from pyrogram import filters
from pyrogram.errors import UserNotParticipant

from main import app
from config import FORCE_SUB

@app.on_message(filters.private)
async def force_subscribe(client, message):

    try:
        user = await app.get_chat_member(
            FORCE_SUB,
            message.from_user.id
        )

    except UserNotParticipant:

        return await message.reply_text(
            f"⚠️ Join @{FORCE_SUB} First"
        )# Force sub handler
