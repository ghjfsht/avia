import os
import time
import logging
from telegram import Bot
from scraper import get_latest_odds

bot = Bot(token=os.getenv("BOT_TOKEN"))
chat_id = os.getenv("CHAT_ID")

logging.basicConfig(level=logging.INFO)

def main():
    last_odd = 1.0
    while True:
        try:
            current_odd = get_latest_odds()
            if current_odd > 2.0 and last_odd <= 2.0:
                bot.send_message(chat_id=chat_id, text=f"Yangi koeffitsiyent: {current_odd}x")
            last_odd = current_odd
        except Exception as e:
            logging.error(f"Xatolik: {e}")
        time.sleep(10)

if __name__ == "__main__":
    main()
