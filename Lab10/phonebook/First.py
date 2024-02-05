import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="Uakkes04", port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)


def change_phone():
    name1 = input("Enter your name: ")
    phone_num = int(input("Enter your phone number: "))
    cur.execute("""UPDATE phonebook SET number=%s WHERE name=%s;""", (phone_num, name1))


def change_name():
    name1 = input("Enter your name: ")
    phone_num = int(input("Enter your phone number: "))
    cur.execute("""UPDATE phonebook SET name=%s WHERE number=%s;""", (name1, phone_num))


def insert_user():
    name1 = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    cur.execute("""INSERT INTO phonebook (number, name) VALUES
    (%s, %s)""", (phone, name1))


def query():
    cur.execute("""SELECT * FROM phonebook;""")
    lst = cur.fetchall()
    for row in lst:
        print(row)


def delete_user_name():
    name1 = input("Enter your name: ")
    cur.execute("""DELETE FROM phonebook WHERE name=%s;""", (name1, ))


def delete_user_phone():
    phone_num = input("Enter your phone number: ")
    cur.execute("""DELETE FROM phonebook WHERE number=%s;""", (phone_num, ))


cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
number INT PRIMARY KEY,
name VARCHAR(255)
);
""")

# insert_user()

# change_name()

# query()

# delete_user_name()

# delete_user_phone()

conn.commit()

cur.close()
conn.close()
