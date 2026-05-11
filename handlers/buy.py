from pyrogram import filters

from bot import app
from config import PLAN_PRICE

@app.on_message(filters.command("buy"))
async def buy(client, message):

    text = f"""
💎 PREMIUM PLAN

📅 Duration : 30 Days
🎥 Daily Limit : 100 Videos

💰 Price : ₹{PLAN_PRICE}

🟢 UPI Payment:
upi://pay?pa=yourupi@upi

📤 Send Screenshot After Payment
"""

    await message.reply_text(text)# Buy handler
