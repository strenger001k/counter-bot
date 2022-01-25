from bot import bot
from db import *
import psycopg2
from config import DB_URI

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username

    bot.reply_to(message, "hi!!!")
    regestration(message.from_user.id, username)
    update_messages_count(message.from_user.id)


@bot.message_handler(commands=["stats"])
def get_stats(message):
    # bot.reply_to(message, "get_stats_messsage()")
    bot.reply_to(message, get_stats_messsage(), disable_web_page_preview=True, parse_mode="HTML",)
    update_messages_count(message.from_user.id)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def message_from_user(message):
    update_messages_count(message.from_user.id)
