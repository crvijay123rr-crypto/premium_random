from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

from bot import app
from database.users_db import add_user
from database.mongo import users

# IMPORT FUNCTIONS
from handlers.videos import send_videos
from handlers.demo import demo
from handlers.buy import buy
from handlers.myplan import myplan

CHANNEL_USERNAME = "BOTUPDATEDARK"

START_TEXT = """
╔════════════════╗
   👑 PREMIUM HUB 👑
╚════════════════╝

🔥 Unlimited Random Videos
⚡ Daily 200 Videos
🛡 Protected Content
💎 Monthly VIP Access

🎥 Videos Saved In Database
Only For 30 Days
"""

START_PIC = "assets/banner.jpg"


# =========================
# CHECK CHANNEL JOIN
# =========================
async def is_joined(client, user_id):

    try:

        await client.get_chat_member(
            CHANNEL_USERNAME,
            user_id
        )

        return True

    except UserNotParticipant:

        return False

    except:

        return False


# =========================
# START COMMAND
# =========================
@app.on_message(filters.command("start"))
async def start(client, message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name

    joined = await is_joined(
        client,
        user_id
    )

    # USER NOT JOINED
    if not joined:

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📢 JOIN NOW",
                    url="https://t.me/BOTUPDATEDARK"
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
    await add_user(user_id)

    # SAVE USER NAME
    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "name": first_name
            }
        }
    )

    # MAIN MENU
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


# =========================
# TRY AGAIN BUTTON
# =========================
@app.on_callback_query(filters.regex("^check_join$"))
async def check_join(client, query):

    joined = await is_joined(
        client,
        query.from_user.id
    )

    # STILL NOT JOINED
    if not joined:

        return await query.answer(
            "❌ Join Channel First",
            show_alert=True
        )

    # MAIN MENU
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 GET VIDEOS", callback_data="videos")],
        [InlineKeyboardButton("🎁 FREE DEMO", callback_data="demo")],
        [InlineKeyboardButton("💳 BUY PREMIUM", callback_data="buy")],
        [InlineKeyboardButton("📊 MY PLAN", callback_data="myplan")],
        [InlineKeyboardButton("☎ SUPPORT", url="https://t.me/Contact_45bot")]
    ])

    try:
        await query.message.delete()

    except:
        pass

    await query.message.reply_photo(
        photo=START_PIC,
        caption=START_TEXT,
        reply_markup=buttons
    )

    await query.answer(
        "✅ Access Granted"
    )


# =========================
# GET VIDEOS BUTTON
# =========================
@app.on_callback_query(filters.regex("^videos$"))
async def videos_callback(client, query):

    await query.answer(
        "⚡ Sending Videos..."
    )

    await send_videos(
        client,
        query.message
    )


# =========================
# DEMO BUTTON
# =========================
@app.on_callback_query(filters.regex("^demo$"))
async def demo_callback(client, query):

    await query.answer(
        "🎁 Sending Demo..."
    )

    await demo(
        client,
        query.message
    )


# =========================
# BUY BUTTON
# =========================
@app.on_callback_query(filters.regex("^buy$"))
async def buy_callback(client, query):

    await query.answer()

    await buy(
        client,
        query.message
    )


# =========================
# MY PLAN BUTTON
# =========================
@app.on_callback_query(filters.regex("^myplan$"))
async def myplan_callback(client, query):

    await query.answer()

    await myplan(
        client,
        query.message
   )    ])

    try:
        await query.message.delete()

    except:
        pass

    await query.message.reply_photo(
        photo=START_PIC,
        caption=START_TEXT,
        reply_markup=buttons
    )

    await query.answer(
        "✅ Access Granted"
    )


# =========================
# GET VIDEOS BUTTON
# =========================
@app.on_callback_query(filters.regex("^videos$"))
async def videos_callback(client, query):

    await query.answer(
        "⚡ Sending Videos..."
    )

    await send_videos(
        client,
        query.message
    )


# =========================
# DEMO BUTTON
# =========================
@app.on_callback_query(filters.regex("^demo$"))
async def demo_callback(client, query):

    await query.answer(
        "🎁 Sending Demo..."
    )

    await demo(
        client,
        query.message
    )


# =========================
# BUY BUTTON
# =========================
@app.on_callback_query(filters.regex("^buy$"))
async def buy_callback(client, query):

    await query.answer()

    await buy(
        client,
        query.message
    )


# =========================
# MY PLAN BUTTON
# =========================
@app.on_callback_query(filters.regex("^myplan$"))
async def myplan_callback(client, query):

    await query.answer()

    await myplan(
        client,
        query.message
)
