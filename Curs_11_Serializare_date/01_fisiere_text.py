"""
Serializarea datelor --> se doreste persistarea datelor din aplicatie pentru a fi disponibile
                         in viitor pentru a putea fi citite sau modificate
"""


# Citire date in mod clasic
# se foloseste intotdeauna try except, ca sa verifice daca are erori in fisier
def read_clasic():
    f = open("data.txt", "r")  # deschiderea fisierului si retinerea lui in variabila 'f'
    try:
        return f.readlines()  # citim toate datele din fisier
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        f.close()  # inchidem fisierul


l = read_clasic()
print(l)

print("-" * 40)


# Citire folosind ContextManager

def read_safe():
    with open("data.txt", "r") as f:
        return f.readlines()


l = read_safe()
print(l)

print("-" * 40)

# Scriere date in fisier
# suprascrie tot continutul anterior (se pierd datele care au fost inainte)
def write():
    with open("data.txt", "w") as f:
        f.writelines(["1\n", "abc","1 2 3\n"])

write()

# Adaugare date in fisier

def append():
    with open("data.txt", "a") as f:
        f.writelines(["test ", "word2 ", "word3"])

append()