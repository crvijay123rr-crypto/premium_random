from dotenv import load_dotenv
import os
load_dotenv()

API_ID=int(os.getenv("API_ID"))
API_HASH=os.getenv("API_HASH")
BOT_TOKEN=os.getenv("BOT_TOKEN")
MONGO_URI=os.getenv("MONGO_URI")
OWNER_ID=int(os.getenv("OWNER_ID"))
LOG_CHANNEL=int(os.getenv("LOG_CHANNEL"))
FORCE_SUB=os.getenv("FORCE_SUB")
PREMIUM_CHANNEL=int(os.getenv("PREMIUM_CHANNEL"))
DEMO_CHANNEL=int(os.getenv("DEMO_CHANNEL"))

DAILY_LIMIT=100
DEMO_LIMIT=50
PLAN_PRICE=200
