from pyrogram import filters

from config import OWNER_ID

# ADMIN FILTER
admin_filter = filters.user(
    OWNER_ID
)
