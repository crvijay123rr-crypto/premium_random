from pyrogram.filters import create
from pyrogram.errors import UserNotParticipant

from main import app
from config import FORCE_SUB

# FORCE SUB FILTER
async def subscribed_func(
    flt,
    client,
    message
):

    try:

        await app.get_chat_member(
            FORCE_SUB,
            message.from_user.id
        )

        return True

    except UserNotParticipant:

        await message.reply_text(
            f"""
⚠️ Join Channel First

https://t.me/{FORCE_SUB}
"""
        )

        return False

subscribed_filter = create(
    subscribed_func
)
