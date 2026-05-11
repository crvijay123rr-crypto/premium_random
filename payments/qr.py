import qrcode

from payments.upi import upi_link

# GENERATE QR
def generate_qr(user_id):

    link = upi_link(user_id)

    qr = qrcode.make(link)

    path = f"temp/qr_{user_id}.png"

    qr.save(path)

    return path
