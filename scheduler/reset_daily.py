from database.users_db import reset_daily

async def reset_daily_limits():

    try:

        await reset_daily()

        print("✅ Daily Limits Reset")

    except Exception as e:

        print(f"❌ Reset Error : {e}")
