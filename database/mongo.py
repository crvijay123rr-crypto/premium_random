from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

mongo = AsyncIOMotorClient(MONGO_URI)

db = mongo["PREMIUM_RANDOM_VIDEO_BOT"]

users = db.users
videos = db.videos
plans = db.plans
stats = db.stats
