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
    db_object.execute("SELECT * FROM users ORDER BY messages DESC LIMIT 10")
    result = db_object.fetchall()

    if not result:
        bot.reply_to(message, "No data...")
    else:
        reply_message = "- Top flooders:\n"
        for i, item in enumerate(result):
            reply_message += f"[{i + 1}] {item[1].strip()} ({item[0]}) : {item[2]} messages.\n"
        bot.reply_to(message, reply_message)

    user_id = message.from_user.id
    update_messages_count(user_id)