from pyrogram.filters import create

from database.users_db import (
    is_premium
)

# PREMIUM FILTER
async def premium_func(
    flt,
    client,
    message
):

    premium = await is_premium(
        message.from_user.id
    )

    return premium

premium_filter = create(
    premium_func
)
