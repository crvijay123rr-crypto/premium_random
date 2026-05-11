import json

from database.mongo import (
    users,
    videos,
    plans
)

# USERS BACKUP
async def backup_users():

    data = []

    async for user in users.find():

        user["_id"] = str(
            user["_id"]
        )

        data.append(user)

    with open(
        "backups/users_backup.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {"users": data},
            file,
            indent=4
        )

    print("✅ Users Backup Done")

# VIDEOS BACKUP
async def backup_videos():

    data = []

    async for video in videos.find():

        video["_id"] = str(
            video["_id"]
        )

        data.append(video)

    with open(
        "backups/videos_backup.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {"videos": data},
            file,
            indent=4
        )

    print("✅ Videos Backup Done")

# PLANS BACKUP
async def backup_plans():

    data = []

    async for plan in plans.find():

        plan["_id"] = str(
            plan["_id"]
        )

        data.append(plan)

    with open(
        "backups/plans_backup.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {"plans": data},
            file,
            indent=4
        )

    print("✅ Plans Backup Done")

# FULL BACKUP
async def full_backup():

    await backup_users()

    await backup_videos()

    await backup_plans()

    print("🔥 FULL BACKUP COMPLETED")
