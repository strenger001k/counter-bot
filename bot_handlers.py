from bot import bot
from db import *
import psycopg2
from config import DB_URI

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "hi!!!")
    regestration(message.from_user.id, message.from_user.username)
    update_messages_count(message.from_user.id)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def message_from_user(message):
    update_messages_count(message.from_user.id)


@bot.message_handler(commands=["stats"])
def get_stats(message):
    db_object.execute("SELECT * FROM users ORDER BY messages DESC LIMIT 10")
    result = db_object.fetchall()

    if not result:
        bot.reply_to(message, "No data...")
    else:
        reply_message = "- Top flooders:\n"
        for i, item in enumerate(result):
            reply_message += f"[{i + 1}] {item[1].strip()} ({item[0]}) : {item[2]} messages.\n"
        bot.reply_to(message, reply_message)

    update_messages_count(message.from_user.id)