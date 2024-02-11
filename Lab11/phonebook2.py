import math

import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="Uakkes04", port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)


def insert_from_csv(path):
    with open(path) as csvfile:
        for line in csvfile:
            lst = line.strip().split(";")
            if lst[0].isnumeric():
                cur.execute("""INSERT INTO phonebook2 (number, name, surname) VALUES
                (%s, %s, %s)""", (lst[0], lst[1], lst[2]))


def change_phone():
    name1 = input("Enter your name: ")
    phone_num = int(input("Enter your phone number: "))
    cur.execute("""UPDATE phonebook2 SET number=%s WHERE name=%s;""", (phone_num, name1))


def insert_list(lst):
    for row in lst:
        if len(str(row[0])) != 11 and str(row[0])[0] != "8":
            print(f"Please enter a valid phone number instead of {row[0]}")
        else:
            cur.execute("""INSERT INTO phonebook2 (number, name, surname) VALUES 
            (%s, %s, %s)""", (row[0], row[1], row[2]))


def change_name():
    name1 = input("Enter your name: ")
    phone_num = int(input("Enter your phone number: "))
    cur.execute("""UPDATE phonebook2 SET name=%s WHERE number=%s;""", (name1, phone_num))


def insert_user():
    name1 = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    surname1 = input("Enter your surname: ")

    lst = cur.execute("""SELECT number FROM phonebook2 WHERE name = %s""", (name1,))
    if cur.fetchone() is not None:
        cur.execute("""UPDATE phonebook2 SET number=%s WHERE name=%s;""", (phone, name1))
    elif len(phone) != 11 and phone[0] != 8:
        print("Please enter a valid phone")
    else:
        cur.execute("""INSERT INTO phonebook2 (number, name, surname) VALUES
        (%s, %s, %s)""", (phone, name1, surname1))


def query():
    done = False
    cur.execute("""SELECT * FROM phonebook2;""")
    lst = cur.fetchall()
    offset = int(input("Enter a number of data in one page: "))
    print(f"There are {math.ceil(len(lst) / offset)} pages")
    while not done:
        page = input("Enter a page number to search: ")
        if page.isdigit():
            page = int(page)-1
            for row, index in enumerate(lst, len(lst)):
                if page * offset <= row - len(lst) <= page * offset + offset - 1:
                    print(row - len(lst) + 1, "|", index)
        else:
            done = True


def delete_user_name():
    name1 = input("Enter your name: ")
    cur.execute("""DELETE FROM phonebook2 WHERE name=%s;""", (name1,))


def search_by_pattern(name, surname, phone_num):
    cur.execute(f"""SELECT * FROM phonebook2 WHERE name LIKE '%{name}%'""")
    lst1 = cur.fetchall()
    cur.execute(f"""SELECT * FROM phonebook2 WHERE surname LIKE  '%{surname}%'""")
    lst2 = cur.fetchall()
    cur.execute(f"""SELECT * FROM phonebook2 WHERE number LIKE  '%{phone_num}%'""")
    lst3 = cur.fetchall()
    lst1.extend(lst2)
    lst1.extend(lst3)
    lst1 = set(lst1)
    for row in lst1:
        print(row)


def delete_user_phone():
    phone_num = input("Enter your phone number: ")
    cur.execute("""DELETE FROM phonebook2 WHERE number=%s;""", (phone_num,))


cur.execute("""CREATE TABLE IF NOT EXISTS phonebook2 (
number VARCHAR(255) PRIMARY KEY,
name VARCHAR(255),
surname VARCHAR(255)
);
""")

lst1 = [[87021234567, 'Uaks', 'SS'],
        [82384211111, 'Qwer', 'GHS'],
        [82384232586, 'Qwerty', 'Kasd'],
        [82384232516, 'Uali', 'Sopygali'],
        [87002123567, 'Serik', 'Sanzhar'],
        [87019876543, 'Random', 'Random2'],
        [87021235697, 'Hello', 'World'],
        [87002523567, 'Good', 'Job']]

# search_by_pattern('al', 'Kas', '8')

# insert_from_csv('Book2.csv')

# insert_user()

# insert_list(lst1)

# change_name()

# query()

# delete_user_name()

# delete_user_phone()

conn.commit()

cur.close()
conn.close()
