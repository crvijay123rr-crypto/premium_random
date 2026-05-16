from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URI = os.getenv("MONGO_URI")

OWNER_ID = int(os.getenv("OWNER_ID"))

# PREMIUM USERS IDS
PREMIUM_IDS = [
    OWNER_ID,

    7842404760,
    #987654321,
    #741852963,
    #852456123,
    #963258741

    # ADD MORE IDS
]

LOG_CHANNEL = os.getenv("LOG_CHANNEL")

FORCE_SUB = os.getenv("FORCE_SUB")
PREMIUM_CHANNEL = os.getenv("PREMIUM_CHANNEL")
DEMO_CHANNEL = os.getenv("DEMO_CHANNEL")

DAILY_LIMIT = 2
DEMO_LIMIT = 2
PLAN_PRICE = 125
