from bot import bot
from db import *
from config import CONTENT_TYPES
from messages import GREETING


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, GREETING)
    if not message.from_user.username:
        regestration(message.from_user.id,
                     message.from_user.first_name,
                     str(message.chat.id))
    else:
        regestration(message.from_user.id,
                     message.from_user.username,
                     str(message.chat.id))


@bot.message_handler(commands=["stats"])
def get_stats(message):
    bot.reply_to(message,
                 get_stats_messsage(str(message.chat.id)),
                 disable_web_page_preview=True,
                 parse_mode="HTML")


@bot.message_handler(content_types=CONTENT_TYPES)
def message_from_user(message):
    update_messages_count(message.from_user.id, str(message.chat.id))


@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    name = message.new_chat_participant.first_name
    print(name)
    bot.reply_to(message, 'welcome')
