from bot import bot
# from db import *
import psycopg2
from config import DB_URI

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()


def update_messages_count(user_id):
    db_object.execute(f"UPDATE users SET messages = messages + 1 WHERE id = {user_id}")
    db_connection.commit()


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    bot.reply_to(message, f"Hello, {username}!")

    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()

    if not result:
        db_object.execute("INSERT INTO users(id, username, messages) VALUES (%s, %s, %s)", (user_id, username, 0))
        db_connection.commit()

    update_messages_count(user_id)


@bot.message_handler(commands=["stats"])
def get_stats(message):
    # db_object.execute("SELECT * FROM users ORDER BY messages ASC")
    # users = db_object.fetchall()
    bot.send_message(message.chat.id, "users")
    # if not users:
    #     bot.reply_to(message, "No data...")
    # else:
    #     print(users)
    #     list_all_users = []
    #     for user in users:
    #         list_all_users.append(user[0], user[1], user[2])
    #     bot.reply_to(message, ''.join(list_all_users))

    update_messages_count(message.from_user.id)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def message_from_user(message):
    user_id = message.from_user.id
    update_messages_count(user_id)
