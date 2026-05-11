from functools import wraps

from database.users_db import (
    get_user,
    is_premium
)

# PREMIUM REQUIRED
def premium_required(func):

    @wraps(func)
    async def wrapper(client, message):

        premium = await is_premium(
            message.from_user.id
        )

        if not premium:

            return await message.reply_text(
                "❌ Premium Required"
            )

        return await func(
            client,
            message
        )

    return wrapper

# NOT BANNED
def not_banned(func):

    @wraps(func)
    async def wrapper(client, message):

        user = await get_user(
            message.from_user.id
        )

        if user and user.get("banned"):

            return await message.reply_text(
                "❌ You Are Banned"
            )

        return await func(
            client,
            message
        )

    return wrapper
