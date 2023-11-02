import sqlite3
from pprint import pprint
conn = sqlite3.connect("students.db") #deschidem o conexiune la baza de date
cursor = conn.cursor()

#returnam numele materia si nota pentru un student

querry ="""
SELECT s.name, g.topic, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.name=?;
"""

cursor.execute(querry,("Eva",))
pprint(cursor.fetchall())