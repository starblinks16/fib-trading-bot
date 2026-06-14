import requests

BOT_TOKEN = "8517898625:AAEZmk1kSNm82PihpmudLtaRtO6xpRUqw5E"
CHAT_ID = "7588696401"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "✅ Test message from GitHub"
    }
)

print(response.status_code)
print(response.text)
