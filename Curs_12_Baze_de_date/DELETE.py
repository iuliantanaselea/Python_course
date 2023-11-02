import sqlite3
from pprint import pprint
conn = sqlite3.connect("students.db") #deschidem o conexiune la baza de date
cursor = conn.cursor()

querry= """
DELETE FROM grades
WHERE topic=:topic and student_id=:id;
"""
cursor.execute(querry, {'topic': 'webdev', 'id': 1})
conn.commit()
cursor.execute('SELECT * FROM grades')
pprint(cursor.fetchall())