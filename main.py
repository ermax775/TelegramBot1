# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# print("Hello")

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import logging
from telegram.ext import *
import responses2

API_KEY = '1929402337:AAFIJYbEaw8rwDNLdF2vKNem_ISdkz6-lJk'

# Set Up the logging proc...
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting bot...')

def start_cmd(update, context):
    update.message.reply_text(" Welcome to the chat bot, safely. You\'re in safe hands now. Just Chill.")

def help_cmd(update, context):
    update.message.reply_text(" Welcome to the chat bot, safely. We\'ll make sure your request will be satisfied soon.")

def custom_cmd(update, context):
    update.message.reply_text(" Join Tekle on his blog site https://tekbelblog.wordpress.com/ ")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses2.get_response(text)
    logging.info(f'User({update.message.chat.id}) says: {text}')

    #Bot Response
    update.message.reply_text(response)

def error(update, context):
    logging.error(f'Update{update} caused error{context.error}')

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    #Commands
    dp.add_handler(CommandHandler('start', start_cmd))
    dp.add_handler(CommandHandler('help', help_cmd))
    dp.add_handler(CommandHandler('custom', custom_cmd))

    #Messages
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    #Errors
    dp.add_error_handler(error)

    #Running the Bot, now:
    updater.start_polling(2.0)
    updater.idle()






