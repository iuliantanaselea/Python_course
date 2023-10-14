# a=1/0         ZeroDivisionError: division by zero
# a = 2+b       NameError: name 'b' is not defined

#############################################################
# Aruncarea exceptiilor (Raise exception)

x = 2
if x < 0:
    raise Exception("x < 0")

#############################################################
# Tratarea exceptiilor

try:  # verifica un bloc de cod pentru exceptii
    print(c)
except:  # Trateaza diferitele tipuri de erori
    print("A aparut o exceptie")

# -------------------------------------------------------------

try:
    print(1 / 0)
except NameError:
    print("Variabila c nu este definita")
except ZeroDivisionError as ex:  # Stocheaza exceptia in variabila ex
    print(f"Eroarea: {ex}")
except:
    print("Alta a fost eroarea")

# -------------------------------------------------------------
try:
    print('Hello')
except:
    print("Eroare")
else:
    print("Se executa cand nu apare eroarea")
# Ramura try, except, else este folosita pt a rula o bucata de cod daca nu apare eroare in blocul try

try:
    print('c')
except:
    print("Eroare")
finally:
    print("Eu ma execut mereu")  # Finally se executa de fiecare data, indiferent daca este eroare sau nu

#############################################################
"""
try: (blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: --> Prinderea tuturor exceptiilor de tipul NumeEroare
    Se executa doar daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): -->Gruparea mai multor tipuri de exceptii
    Se executa doar daca se prinde una dintre cele doua erori
except Eroarea4 as ex: --> Stocarea mesajului unei erori intr-o variabila
    Se poate accesa mesajul erorii prin variabila ex
except:
    Se executa pentru orice alt tip de eroare nespecificat
else:
    Se executa doar daca nu se arunca eroare in blocul try
finally:
    Se executa indiferent daca se arunca eroare sau nu
"""
