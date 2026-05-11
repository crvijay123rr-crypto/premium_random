from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.reset_daily import reset_daily_limits
from scheduler.expiry import remove_expired_users
from scheduler.cleanup import cleanup_demo

scheduler = AsyncIOScheduler()

# RESET DAILY LIMITS
scheduler.add_job(
    reset_daily_limits,
    "cron",
    hour=0,
    minute=0
)

# REMOVE EXPIRED USERS
scheduler.add_job(
    remove_expired_users,
    "interval",
    hours=1
)

# CLEANUP TASK
scheduler.add_job(
    cleanup_demo,
    "interval",
    minutes=30
)

def start_scheduler():

    scheduler.start()

    print("✅ Scheduler Started")
