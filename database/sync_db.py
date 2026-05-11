from database.mongo import db

sync_data = db.sync_data


async def get_last_msg():

    data = await sync_data.find_one({})

    if not data:
        return 0

    return data.get("last_msg_id", 0)


async def save_last_msg(msg_id):

    await sync_data.update_one(
        {},
        {
            "$set": {
                "last_msg_id": msg_id
            }
        },
        upsert=True
    )
