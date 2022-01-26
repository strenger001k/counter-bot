import psycopg2
from config import DB_URI

db_connection = psycopg2.connect(DB_URI)
db_object = db_connection.cursor()


def repea_group(users, group):
    for user in users:
        if user[1].strip() == group:
            return True


def regestration(user_id, username, group):
    db_object.execute(f"SELECT * FROM users WHERE id = {user_id}")
    id_user = db_object.fetchall()
    if id_user:
        if not repea_group(id_user, group):
            db_object.execute("INSERT INTO users (id, group_id, username) VALUES (%s, %s, %s)", (user_id, group, username))
            db_connection.commit()
    else:
        db_object.execute("INSERT INTO users (id, group_id, username) VALUES (%s, %s, %s)", (user_id, group, username))
        db_connection.commit()


def update_messages_count(user_id, group):
    db_object.execute(f"UPDATE users SET message = message + 1 WHERE id = {user_id} AND group_id LIKE '%{group}%'")
    db_connection.commit()


def get_stats_messsage(group):
    db_object.execute("SELECT * FROM users ORDER BY message DESC LIMIT 10")
    users = db_object.fetchall()
    if users:
        reply_message = "Top flooders:\n"
        for user in users:
            if user[1].strip() == group:
                reply_message += f'<a href="https://t.me/{user[2].strip()}">{user[2].strip()}</a> - {user[3]} messages\n'
    else:
        reply_message = "No data..."
    return reply_message
