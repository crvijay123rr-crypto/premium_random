from pyrogram.filters import create

from database.users_db import (
    get_user
)

# BANNED FILTER
async def banned_func(
    flt,
    client,
    message
):

    user = await get_user(
        message.from_user.id
    )

    if not user:
        return True

    return not user.get(
        "banned",
        False
    )

banned_filter = create(
    banned_func
)
