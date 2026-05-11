from pyrogram import filters
from config import OWNER_ID

admin_filter = filters.user(int(OWNER_ID))
