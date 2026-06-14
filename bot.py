import requests

BOT_TOKEN = "8517898625:AAEEH8mFW06rxvLAwVEFMWoRrROyWUCWABU"
CHAT_ID = "7588696401"

message = "✅ Hello starblinks! Your GitHub bot is connected."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Message sent")
