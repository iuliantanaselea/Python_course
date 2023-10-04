# OPERATORI DE COMPARARE

# Operatori de comparare exacta: "==" - Returneaza boolean true/false
nume = "Creanga"
alt_nume = "creanga"

print(nume == alt_nume)

alt_nume = alt_nume.capitalize()
print(nume == alt_nume)

print("-" * 40)

# Operatori de diferentiere: "!="
a, b = 10, 11

print(a != b)

print("-" * 40)
# Operatori de comparare: ">", "<", ">=", "<="
print(a < b)
print(a > b)
print("a <= b ", a <= b)
print(a >= b)