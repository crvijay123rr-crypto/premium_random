from database.mongo import users, videos

# TOTAL USERS
async def total_users():

    return await users.count_documents({})

# TOTAL PREMIUM USERS
async def total_premium_users():

    return await users.count_documents({
        "premium": True
    })

# TOTAL BANNED USERS
async def total_banned_users():

    return await users.count_documents({
        "banned": True
    })

# TOTAL VIDEOS
async def total_videos():

    return await videos.count_documents({
        "demo": False
    })

# TOTAL DEMO VIDEOS
async def total_demo_videos():

    return await videos.count_documents({
        "demo": True
    })# Stats DB functions
