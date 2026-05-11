from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import app
from config import FORCE_SUB
from database.users_db import add_user


START_TEXT = """
╔════════════════╗
   👑 PREMIUM HUB 👑
╚════════════════╝

🔥 Unlimited Random Videos
⚡ Daily 100 Videos
🛡 Protected Content
💎 Monthly VIP Access 🎥videos saved your database only 30 days 
"""

START_PIC = "assets/banner.jpg"


# FORCE SUB CHECK
async def check_force_sub(client, user_id):

    try:
        member = await client.get_chat_member(
            FORCE_SUB,
            user_id
        )

        if member.status in [
            "member",
            "administrator",
            "creator"
        ]:
            return True

    except:
        return False

    return False


@app.on_message(filters.command("start"))
async def start(client, message):

    user_id = message.from_user.id

    # CHECK CHANNEL JOIN
    joined = await check_force_sub(client, user_id)

    # NOT JOINED
    if not joined:

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📢 JOIN NOW",
                    url=f"https://t.me/{FORCE_SUB.replace('@', '')}"
                )
            ],
            [
                InlineKeyboardButton(
                    "✅ TRY AGAIN",
                    callback_data="check_join"
                )
            ]
        ])

        return await message.reply_photo(
            photo=START_PIC,
            caption="""
⚠️ You Must Join Our Channel First

🔒 Join Required To Access Bot

👇 Click Below To Join
""",
            reply_markup=buttons
        )

    # ADD USER
    try:
        await add_user(user_id)

    except Exception as e:
        print(f"ADD USER ERROR: {e}")

    # MAIN BUTTONS
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 GET VIDEOS", callback_data="videos")],
        [InlineKeyboardButton("🎁 FREE DEMO", callback_data="demo")],
        [InlineKeyboardButton("💳 BUY PREMIUM", callback_data="buy")],
        [InlineKeyboardButton("📊 MY PLAN", callback_data="myplan")],
        [InlineKeyboardButton("☎ SUPPORT", url="https://t.me/Contact_45bot")]
    ])

    await message.reply_photo(
        photo=START_PIC,
        caption=START_TEXT,
        reply_markup=buttons
    )


# TRY AGAIN BUTTON
@app.on_callback_query(filters.regex("check_join"))
async def check_join_callback(client, query):

    joined = await check_force_sub(
        client,
        query.from_user.id
    )

    if not joined:

        return await query.answer(
            "❌ Please Join Channel First",
            show_alert=True
        )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 GET VIDEOS", callback_data="videos")],
        [InlineKeyboardButton("🎁 FREE DEMO", callback_data="demo")],
        [InlineKeyboardButton("💳 BUY PREMIUM", callback_data="buy")],
        [InlineKeyboardButton("📊 MY PLAN", callback_data="myplan")],
        [InlineKeyboardButton("☎ SUPPORT", url="https://t.me/Contact_45bot")]
    ])

    await query.message.edit_caption(
        caption=START_TEXT,
        reply_markup=buttons
    )

    await query.answer("✅ Access Granted")
