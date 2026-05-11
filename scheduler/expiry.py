from datetime import datetime

from database.mongo import users

async def remove_expired_users():

    try:

        premium_users = users.find({
            "premium": True
        })

        async for user in premium_users:

            expiry = user.get("expiry")

            if not expiry:
                continue

            if expiry < datetime.utcnow():

                await users.update_one(
                    {"user_id": user["user_id"]},
                    {
                        "$set": {
                            "premium": False,
                            "expiry": None
                        }
                    }
                )

                print(
                    f"❌ Premium Expired : {user['user_id']}"
                )

    except Exception as e:

        print(f"❌ Expiry Error : {e}")
