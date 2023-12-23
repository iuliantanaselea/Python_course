"""
Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
try - finally
Fișierul se deschide înainte de try, folosind functia open
În interiorul try citim conținutul folosind functia read
În finally se închide fișierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul face asta pentru noi.

"""
# Varianta 1

f = open('hello.txt', 'r')
try:
    print(f.read())
finally:
    f.close()

print("-" * 40)

# Varianta 2

with open("hello.txt", 'r') as file:
    print(file.read())
