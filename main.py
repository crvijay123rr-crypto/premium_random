from pyrogram import Client
from config import *

app = Client(
    "PremiumBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

try:
    import handlers.start
    print("start loaded")

    import handlers.videos
    print("videos loaded")

    import handlers.demo
    print("demo loaded")

    import handlers.buy
    print("buy loaded")

    import handlers.myplan
    print("myplan loaded")

    import handlers.support
    print("support loaded")

    import handlers.referral
    print("referral loaded")

    import handlers.redeem
    print("redeem loaded")

    import handlers.callbacks
    print("callbacks loaded")

    import handlers.force_sub
    print("force_sub loaded")

except Exception as e:
    print(e)

print("BOT STARTED")

app.run()
