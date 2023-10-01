# TYPE CASTING
#  functia type() returneaza tipul variabilei sau a datei (int, float, boolean)

nume_complet, valoare = "Ion Creanga", True

print(type(nume_complet))
print(type(valoare))

# TYPE CASTING - schimbarea tipului variabilei
x = 2.712
print(type(x))

y = str(x)  # am schimbat variabila x din float in string
print(type(y))

z = int(x) #am schimbat variabila din float in integer
print(type(z), z )

nume = "Eminescu"
# nume = int(nume)
# print(nume) # eroare pt ca nu stie sa transforme literele, caracterele speciale in cifre. Poate doar numere sa transforme
# ValueError: invalid literal for int() with base 10: 'Eminescu'
