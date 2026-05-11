from pyrogram import filters

from main import app

@app.on_callback_query()
async def callbacks(client, query):

    data = query.data

    if data == "videos":
        await query.message.reply_text(
            "/videos"
        )

    elif data == "demo":
        await query.message.reply_text(
            "/demo"
        )

    elif data == "buy":
        await query.message.reply_text(
            "/buy"
        )

    elif data == "myplan":
        await query.message.reply_text(
            "/myplan"
        )# Callback handler
