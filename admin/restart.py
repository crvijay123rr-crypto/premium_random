import os
import sys

from pyrogram import filters

from main import app
from admin.admin import admin_filter

@app.on_message(filters.command("restart") & admin_filter)
async def restart(client, message):

    await message.reply_text(
        "
