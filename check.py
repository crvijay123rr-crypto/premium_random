from pyrogram import Client

api_id = 24894984
api_hash = "4956e23833905463efb588eb806f9804"

app = Client(
    "userbot",
    api_id=api_id,
    api_hash=api_hash
)

with app:

    # PUBLIC USERNAME
    chat = app.get_chat("pppppppppppptyy")

    print(chat.title)
