import sqlite3
# cheia primara este acel element unic prin care se poate face conexiunea dintre doua elemente
conn = sqlite3.connect("students.db") #deschidem o conexiune la baza de date
cursor = conn.cursor()

c1 = """
CREATE TABLE if not exists students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age>18)
    );
"""
#PRIMARY KEY --> acel camp care identifica unic o intrare dintr-un tabel
#AUTOINCREMENT --> creste automat valoarea campului pe care este setat

c2= """
CREATE TABLE if not exists grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK(0<=grade and grade <=10),
    student_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)    
    );
"""

#FOREIGN KEY --> un camp pus intr-un tabel de legatura pentru a face asocierea cu un alt
                #prin valoarea acelui camp
#FOREIGN KEY(student_id) REFERENCES students(id)  --> nu putem adauga o nota pentru
                                                    #studentul al carui id nu exista

cursor.execute(c1)
cursor.execute(c2)
