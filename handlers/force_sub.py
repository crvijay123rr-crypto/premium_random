from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from main import app
from config import FORCE_SUB


@app.on_message(filters.private, group=1)
async def force_subscribe(client, message):

    try:
        await app.get_chat_member(
            FORCE_SUB,
            message.from_user.id
        )

    except UserNotParticipant:

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🔔 Join Channel",
                    url=f"https://t.me/{FORCE_SUB.replace('@', '')}"
                )
            ]
        ])

        return await message.reply_text(
            "⚠️ Please join our channel first.",
            reply_markup=buttons
        )

    except Exception as e:
        print(e)
