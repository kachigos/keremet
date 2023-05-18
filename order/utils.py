import requests
from decouple import config

def send_telegram_message(message_text):
    chat_id = config('CHAT_ID')
    bot_token = config('BOT_TOKEN')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message_text}
    requests.post(url, json=payload)