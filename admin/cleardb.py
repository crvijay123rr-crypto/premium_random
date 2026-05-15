from pyrogram import filters

from bot import app
from admin.admin import admin_filter

from database.mongo import videos


@app.on_message(filters.command("cleardb") & admin_filter)
async def clear_database(client, message):

    args = message.command

    if len(args) < 2:
        return await message.reply_text(
            """
⚠️ Usage :

/cleardb demo
/cleardb premium
/cleardb all
"""
        )

    mode = args[1].lower()

    # CLEAR DEMO
    if mode == "demo":

        result = await videos.delete_many({
            "demo": True
        })

        return await message.reply_text(
            f"""
╔════════════════════╗
      🗑 DEMO CLEARED
╚════════════════════╝

✅ Deleted :
{result.deleted_count}

🔥 Demo Database Cleaned
"""
        )

    # CLEAR PREMIUM
    elif mode == "premium":

        result = await videos.delete_many({
            "demo": False
        })

        return await message.reply_text(
            f"""
╔════════════════════╗
    🗑 PREMIUM CLEARED
╚════════════════════╝

✅ Deleted :
{result.deleted_count}

🔥 Premium Database Cleaned
"""
        )

    # CLEAR ALL
    elif mode == "all":

        result = await videos.delete_many({})

        return await message.reply_text(
            f"""
╔════════════════════╗
       🗑 ALL CLEARED
╚════════════════════╝

✅ Deleted :
{result.deleted_count}

🔥 Full Database Cleaned
"""
        )

    else:

        return await message.reply_text(
            "❌ Invalid Option"
        )
