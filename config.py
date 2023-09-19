import os

API_ID = int(os.environ.get("API_ID", 28414026))
API_HASH = os.environ.get("595e101e4009da570ae71cae7060d20f", None)
BOT_TOKEN = os.environ.get("6526902074:AAFFUh9pQ-i4wu9j1KsKNdLiWvIz1APb4fA", None)
DB_CHANNEL_ID = os.environ.get("-1001812839961")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("1476002847"))
UPDATE_CHANNEL = os.environ.get('-1001812839961', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
