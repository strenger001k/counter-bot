import psycopg2
from config import DB_URI


db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()


def regestration(user_id, username):
    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()

    if not result:
        db_object.execute("INSERT INTO users(id, username, message) VALUES (%s, %s, %s)", (user_id, username, 0))
        db_connection.commit()


def update_messages_count(user_id):
    db_object.execute(f"UPDATE users SET message = message + 1 WHERE id = {user_id}")
    db_connection.commit()

def get_stats_messsage():
    db_object.execute("SELECT * FROM users ORDER BY messages DESC LIMIT 10")
    result = db_object.fetchall()
    reply_message = "- Top flooders:\n"
    for i, item in enumerate(result):
        reply_message += f"[{i + 1}] {item[1].strip()} ({item[0]}) : {item[2]} messages.\n"
    return reply_message