from config import PLAN_PRICE

# UPI DETAILS
UPI_ID = "yourupi@upi"

# PAYMENT TEXT
def payment_text(user_id):

    return f"""
╔════════════════╗
    💎 PREMIUM PLAN 💎
╚════════════════╝

📅 Duration : 30 Days
🎥 Daily Limit : 100 Videos

💰 Price : ₹{PLAN_PRICE}

🟢 Pay UPI :
{UPI_ID}

⚠️ After Payment Send Screenshot

🆔 USER ID :
{user_id}
"""

# UPI LINK
def upi_link(user_id):

    return (
        f"upi://pay?"
        f"pa={UPI_ID}"
        f"&pn=PremiumHub"
        f"&am={PLAN_PRICE}"
        f"&cu=INR"
        f"&tn=Premium Plan {user_id}"
    )
