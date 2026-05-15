from database.mongo import videos


# ADD PREMIUM VIDEO
async def add_video(channel, msg_id):

    already = await videos.find_one({
        "channel": channel,
        "msg_id": msg_id,
        "demo": False
    })

    # ALREADY EXISTS
    if already:
        return False

    await videos.insert_one({
        "channel": channel,
        "msg_id": msg_id,
        "demo": False
    })

    return True


# ADD DEMO VIDEO
async def add_demo(channel, msg_id):

    already = await videos.find_one({
        "channel": channel,
        "msg_id": msg_id,
        "demo": True
    })

    # ALREADY EXISTS
    if already:
        return False

    await videos.insert_one({
        "channel": channel,
        "msg_id": msg_id,
        "demo": True
    })

    return True


# GET ALL PREMIUM VIDEOS
async def get_all_videos():

    return await videos.find({
        "demo": False
    }).to_list(length=None)


# GET ALL DEMO VIDEOS
async def get_demo_videos():

    return await videos.find({
        "demo": True
    }).to_list(length=None)


# DELETE VIDEO
async def delete_video(msg_id):

    await videos.delete_one({
        "msg_id": msg_id
    })


# TOTAL PREMIUM VIDEOS
async def total_videos():

    return await videos.count_documents({
        "demo": False
    })


# TOTAL DEMO VIDEOS
async def total_demo():

    return await videos.count_documents({
        "demo": True
    })
