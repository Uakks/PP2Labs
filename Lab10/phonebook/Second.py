import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="Uakkes04", port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
number INT PRIMARY KEY,
name VARCHAR(255)
);
""")

path = "Book1.csv"
with open(path) as csvfile:
    for line in csvfile:
        lst = line.strip().split(";")
        if line[0].isnumeric():
            cur.execute("""INSERT INTO phonebook (number, name) VALUES
            (%s, %s)""", (lst[0], lst[1]))

conn.commit()

cur.close()
conn.close()
