import sqlite3
from pprint import pprint
# cheia primara este acel element unic prin care se poate face conexiunea dintre doua elemente
conn = sqlite3.connect("students.db") #deschidem o conexiune la baza de date
cursor = conn.cursor()

cursor.execute(
    """
    SELECT * FROM grades;
    """
)
# pprint(cursor.fetchall())
pprint(cursor.fetchone())
pprint(cursor.fetchone())
pprint(cursor.fetchmany(3))
cursor.execute('SELECT topic, grade FROM grades;')
pprint(cursor.fetchall())

cursor.execute('SELECT * FROM grades WHERE topic=?;', ('web dev',))
pprint(cursor.fetchall())