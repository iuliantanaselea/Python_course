#OPERATORI CONDITIONALI

#operatorii "if", "else"
#sunt operatori de separare a cazurilor in cod

number= 12

if number > 12 :
    print(f"da, {number} este mai mare") #spatiu de identare ( inainte de print) - apartine doar de block-ul 8
else: # daca nu, fac astalalta
    print(f"nu, nu este mai mare") #apartine block-ului "else"
    print("exact")

print("-"*40)
#introducem else if

a = 10
b = 11
if a>b:
    print(f"da, {a} este mai mare decat {b}")
elif a==b:  # se pot introduce "n" CAZURI PARTICULARE
    print("numerele sunt egale")
else:       # implicit rezulta al treilea caz echivalent cu: a<b
    print(f"nu, {a} este mai mic decat {b}")