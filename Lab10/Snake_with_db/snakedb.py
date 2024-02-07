import psycopg2
from pygame.math import Vector2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="Uakkes04", port=5432)

cur = conn.cursor()

# conn.set_session(autocommit=True)


def update_table(username, cur_level):
    cur.execute("""UPDATE snakedb SET current_level = %s WHERE name = %s""", (cur_level, username))
    conn.commit()


def user_exists(username):
    cur.execute("""SELECT current_level FROM snakedb WHERE name = %s""", (username,))
    return cur.fetchone() is not None


def select_user(username):
    cur.execute("""SELECT current_level FROM snakedb WHERE name = %s""", (username,))
    return cur.fetchone()


def insert_row(name1, level):
    cur.execute("""INSERT INTO snakedb (name, current_level) VALUES
    (%s, %s)""", (name1, level))
    conn.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS snakedb (
name VARCHAR(255) PRIMARY KEY,
current_level INT
);
""")


print(user_exists('admin'))

conn.commit()
