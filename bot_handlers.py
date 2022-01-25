from bot import bot
from db import *

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username

    bot.reply_to(message, "hi!!!")
    regestration(user_id)
    update_messages_count(user_id, username)


@bot.message_handler(content_types=["text"])
def message_from_user(message):
    user_id = message.from_user.id
    update_messages_count(user_id)


@bot.message_handler(commands=["stats"])
def get_stats(message):
    bot.reply_to(message, get_messages_count())
    update_messages_count(message.from_user.id)