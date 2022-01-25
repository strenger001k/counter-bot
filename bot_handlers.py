from bot import bot
from db import *

CONTENT_TYPES = ["text",
                 "audio",
                 "document",
                 "photo",
                 "sticker",
                 "video",
                 "video_note",
                 "voice",
                 "location",
                 "contact",
                 ]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "hi!!!")
    regestration(message.from_user.id, message.from_user.username)
    update_messages_count(message.from_user.id)


@bot.message_handler(commands=["stats"])
def get_stats(message):
    bot.reply_to(message,
                 get_stats_messsage(),
                 disable_web_page_preview=True,
                 parse_mode="HTML")
    update_messages_count(message.from_user.id)


@bot.message_handler(content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact"])
def message_from_user(message):
    update_messages_count(message.from_user.id)
