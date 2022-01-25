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