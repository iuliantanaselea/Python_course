# OPERATORI SIMPLI

# OPERATORI DE ASIGNARE "="
a = 5

# OPERATOR DE ADUNARE: operator aritmetic, de string
a, b = "alpha" , "beta"
c = a+b
print(c)

# +, -, *, / - OPERATORI ARITMETICI ( Adunare, scadere, inmultire, impartire)

# RIDICARE LA PUTERE: "**" (De doua ori semnul de inmultire)
baza = 2
exponent = 4
x = baza ** exponent
print(x)

# MODULO - "%" - echivalent cu restul impartirii: 10 (mod 3) = 1
# ne ajuta sa verificam daca un numar este divizibil cu alt numar mai mic
nr = 10
modulo = 3
rest = nr % modulo
print(rest)

y = 20 # este divizibil cu 2?
print("verificam daca este divizibil cu 2: ", y%2) # daca am rezultatul "0" - este divizibil

# IMPARTIRE INTREAGA (de cate ori intra deimpartitul la impartitor)
z = 37
a = 5
print("verificam de cate ori a intra in z: ", z // a) # catul fara rest