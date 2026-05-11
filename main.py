from pyrogram import Client, filters
from config import *

# CREATE BOT CLIENT
app = Client(
    "PremiumBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# LOAD HANDLERS
try:
    import handlers.start
    print("✅ start loaded")

    import handlers.videos
    print("✅ videos loaded")

    import handlers.demo
    print("✅ demo loaded")

    import handlers.buy
    print("✅ buy loaded")

    import handlers.myplan
    print("✅ myplan loaded")

    import handlers.support
    print("✅ support loaded")

    import handlers.referral
    print("✅ referral loaded")

    import handlers.redeem
    print("✅ redeem loaded")

    import handlers.callbacks
    print("✅ callbacks loaded")

    import handlers.force_sub
    print("✅ force_sub loaded")

except Exception as e:
    import traceback
    traceback.print_exc()


# TEST COMMAND
@app.on_message(filters.command("ping"))
async def ping(_, message):
    await message.reply_text("🏓 Pong!")


# DEBUG MESSAGE LOGGER
@app.on_message(filters.all)
async def all_messages(client, message):
    print("MESSAGE RECEIVED:", message.text)


print("🚀 BOT STARTED SUCCESSFULLY")

# RUN BOT
app.run()
