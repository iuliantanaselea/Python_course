import sqlite3
from pprint import pprint
# cheia primara este acel element unic prin care se poate face conexiunea dintre doua elemente
conn = sqlite3.connect("students.db") #deschidem o conexiune la baza de date
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO students(name,email, age)
    VALUES ('Adam', 'adam@genesis.com', 28);
    """
)

cursor.execute(
    """
    INSERT INTO students(name,email, age)
    VALUES ('Eva', 'eva@genesis.com', 25);
    """
)

# conn.commit() #pentru a salva toate datele in baza de date trebuie dat de fiecare data
              # commit la final

cursor.execute(
    """
    SELECT * FROM students;
    """
)

pprint(cursor.fetchall())

grades = [
    ('webdev', 8, 1),
    ('db dev',10,1),
    ('db dev', 8,2),
    ('front end', 10, 2),
    ('web dev',9,2),
    ('web dev',8,2),
    ('web dev',7,1)
    ]

query = """
INSERT INTO grades(topic, grade, student_id)
VALUES (?,?,?)
"""

cursor.executemany(query,grades)
cursor.execute('SELECT * FROM grades')
pprint(cursor.fetchall())
conn.commit()