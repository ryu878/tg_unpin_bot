import telebot
import threading
import time
import datetime


bot = telebot.TeleBot('') # Your Telegram Bot API Key Here
GROUP_CHAT_ID = -100 # Your Group Chat ID


def unpin_periodically():
    while True:
        try:
            # Check for the last pinned message
            chat = bot.get_chat(GROUP_CHAT_ID)
            if chat.pinned_message:
                # If there's a pinned message, unpin it
                bot.unpin_chat_message(GROUP_CHAT_ID)
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f' Unpinned {now}')
        except Exception as e:
            print(f' Error while unpinning: {e}')
        
        # Wait a few seconds before checking again
        time.sleep(5)  # Check every 5 seconds

# Run the unpinning check in a separate thread
unpin_thread = threading.Thread(target=unpin_periodically)
unpin_thread.daemon = True
unpin_thread.start()

# Start polling to keep the bot running
bot.polling()
