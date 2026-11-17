
import os
import json
import urllib.request

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = json.dumps({
        "chat_id": CHAT_ID,
        "text": message
    }).encode()

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request) as response:
        return response.status

if __name__ == "__main__":
    send_message(
        "🎮 Avito GPU Monitor\n"
        "Система анализа видеокарт готова к настройке!"
    )
