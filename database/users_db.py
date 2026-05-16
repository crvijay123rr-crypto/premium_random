from database.mongo import users
from datetime import datetime, timedelta


# =========================
# ADD USER
# =========================
async def add_user(user):

    user_id = user.id

    already = await users.find_one({
        "user_id": user_id
    })

    # USER ALREADY EXISTS
    if already:

        # UPDATE NAME
        await users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "name": user.first_name
                }
            }
        )

        return

    # INSERT NEW USER
    await users.insert_one({
        "user_id": user_id,
        "name": user.first_name,
        "premium": False,
        "expiry": None,
        "used_today": 0,
        "demo_used": 0,
        "last_demo_date": None,
        "banned": False,
        "video_index": 0,
        "total_received": 0,
        "joined": datetime.utcnow()
    })


# =========================
# GET USER
# =========================
async def get_user(user_id):

    return await users.find_one({
        "user_id": user_id
    })


# =========================
# ACTIVATE PREMIUM
# =========================
async def activate_premium(user, days=30):

    # CREATE USER FIRST
    await add_user(user)

    user_id = user.id

    expiry = datetime.utcnow() + timedelta(days=days)

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "premium": True,
                "expiry": expiry,
                "used_today": 0
            }
        }
    )


# =========================
# REMOVE PREMIUM
# =========================
async def remove_premium(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "premium": False,
                "expiry": None
            }
        }
    )


# =========================
# DAILY LIMIT INCREASE
# =========================
async def increase_limit(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$inc": {
                "used_today": 1
            }
        }
    )


# =========================
# DEMO LIMIT INCREASE
# =========================
async def increase_demo(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$inc": {
                "demo_used": 1
            }
        }
    )


# =========================
# RESET DAILY LIMIT
# =========================
async def reset_daily_limit():

    await users.update_many(
        {},
        {
            "$set": {
                "used_today": 0
            }
        }
    )


# =========================
# BAN USER
# =========================
async def ban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": True
            }
        }
    )


# =========================
# UNBAN USER
# =========================
async def unban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": False
            }
        }
    )


# =========================
# CHECK PREMIUM
# =========================
async def is_premium(user_id):

    user = await get_user(user_id)

    # USER NOT FOUND
    if not user:
        return False

    # NOT PREMIUM
    if not user.get("premium", False):
        return False

    expiry = user.get("expiry")

    # EXPIRED
    if expiry and expiry < datetime.utcnow():

        await remove_premium(user_id)

        return False

    return True# =========================
# DEMO LIMIT INCREASE
# =========================
async def increase_demo(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$inc": {
                "demo_used": 1
            }
        }
    )


# =========================
# RESET DAILY LIMIT
# =========================
async def reset_daily_limit():

    await users.update_many(
        {},
        {
            "$set": {
                "used_today": 0
            }
        }
    )


# =========================
# BAN USER
# =========================
async def ban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": True
            }
        }
    )


# =========================
# UNBAN USER
# =========================
async def unban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": False
            }
        }
    )


# =========================
# CHECK PREMIUM
# =========================
async def is_premium(user_id):

    user = await get_user(user_id)

    # USER NOT FOUND
    if not user:
        return False

    # NOT PREMIUM
    if not user.get("premium", False):
        return False

    expiry = user.get("expiry")

    # EXPIRED
    if expiry and expiry < datetime.utcnow():

        await remove_premium(user_id)

        return False

    return Trueasync def unban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": False
            }
        }
    )


# =========================
# CHECK PREMIUM
# =========================
async def is_premium(user_id):

    user = await get_user(user_id)

    # USER NOT FOUND
    if not user:
        return False

    # NOT PREMIUM
    if not user.get("premium", False):
        return False

    expiry = user.get("expiry")

    # EXPIRED
    if expiry and expiry < datetime.utcnow():

        await remove_premium(user_id)

        return False

    return True# =========================
async def reset_daily_limit():

    await users.update_many(
        {},
        {
            "$set": {
                "used_today": 0
            }
        }
    )


# =========================
# BAN USER
# =========================
async def ban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": True
            }
        }
    )


# =========================
# UNBAN USER
# =========================
async def unban_user(user_id):

    await users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "banned": False
            }
        }
    )


# =========================
# CHECK PREMIUM
# =========================
async def is_premium(user_id):

    user = await get_user(user_id)

    # USER NOT FOUND
    if not user:
        return False

    # NOT PREMIUM
    if not user.get("premium", False):
        return False

    expiry = user.get("expiry")

    # EXPIRED
    if expiry and expiry < datetime.utcnow():

        await remove_premium(user_id)

        return False

    return True
