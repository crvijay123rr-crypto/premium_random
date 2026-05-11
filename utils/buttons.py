from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# START BUTTONS
def start_buttons():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🎥 GET VIDEOS",
                callback_data="videos"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 FREE DEMO",
                callback_data="demo"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 BUY PREMIUM",
                callback_data="buy"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 MY PLAN",
                callback_data="myplan"
            )
        ],
        [
            InlineKeyboardButton(
                "☎ SUPPORT",
                url="https://t.me/yourusername"
            )
        ]
    ])

# ADMIN BUTTONS
def admin_buttons():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📊 STATS",
                callback_data="stats"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 BROADCAST",
                callback_data="broadcast"
            )
        ]
    ])
