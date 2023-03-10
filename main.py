import requests
import telegram
from telegram.ext import Updater, CommandHandler

def download_file(url, filename):
    with open(filename, "wb") as f:
        response = requests.get(url)
        f.write(response.content)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Send me a file URL to download.")

def download(update, context):
    url = context.args[0]
    filename = url.split("/")[-1]
    download_file(url, filename)
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(filename, "rb"))

def main():
    # Set up the Telegram API
    token = "6175236410:AAFVNb_1IpLN9Nc6ZDkoYn0TNC-2nhTBrSg"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Add handlers for the commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download))

    # Start the bot
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
