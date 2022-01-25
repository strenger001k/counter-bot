from markupsafe import re
from bot import bot
import psycopg2
from config import DB_URI


db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username

    bot.reply_to(message, "hi!!!")

    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()

    if not result:
        db_object.execute("INSERT INTO users(id, username, message) VALUES (%s, %s, %s)", (user_id, username, 0))
        db_connection.commit()

    # update_messages_count(user_id)


def update_messages_count(user_id):
    db_object.execute(f"UPDATE users SET message = message + 1 WHERE id = {user_id}")
    db_connection.commit() 