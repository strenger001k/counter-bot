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
    db_object.execute("SELECT * FROM users ORDER BY message")
    users = db_object.fetchall()
    if users:
        reply_message = "Top flooders:\n"
        for user in users:
            reply_message += f"{user[1].strip()} ({user[0]}): {user[2]} messages.\n"
    else:
        reply_message = "No data..."
    return reply_message
