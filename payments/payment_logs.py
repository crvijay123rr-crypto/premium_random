from datetime import datetime

# SAVE PAYMENT LOG
def payment_log(user_id, amount):

    with open(
        "logs/payment.log",
        "a",
        encoding="utf-8"
    ) as log:

        log.write(
            f"""
[{datetime.utcnow()}]

USER :
{user_id}

AMOUNT :
₹{amount}

-------------------------
"""
        )
