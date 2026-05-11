from config import PLAN_PRICE

# UPI DETAILS
UPI_ID = "phone pay gift card payment"

# PAYMENT TEXT
def payment_text(user_id):

    return f"""
╔══════════════════════╗
        👑 PREMIUM VIP 👑
╚══════════════════════╝

🔥 Unlock Premium Access Instantly

━━━━━━━━━━━━━━━━━━━

📅 Plan Duration : 30 Days
🎥 Daily Videos : 100
🛡 Protected Content
⚡ Ultra Fast Access

━━━━━━━━━━━━━━━━━━━

💰 Price : ₹{PLAN_PRICE}

💳 PAYMENT METHODS ACCEPTED :

✅ UPI Payment
✅ PhonePe
✅ Google Pay
✅ Paytm
✅ Gift Cards

━━━━━━━━━━━━━━━━━━━

💎 UPI ID :
`{UPI_ID}`

━━━━━━━━━━━━━━━━━━━

⚠️ AFTER PAYMENT

📸 Send Payment Screenshot
🆔 Send Your User ID

🤖 Need Help / Contact :
https://t.me/Contact_45bot

━━━━━━━━━━━━━━━━━━━

🆔 YOUR USER ID :
`{user_id}`

🔥 Enjoy Unlimited Premium Experience
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
