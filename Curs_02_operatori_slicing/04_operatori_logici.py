#OPERATORI LOGICI

# "and"
# Verifica daca toate elementele au aceeasi valoare de adevar
# atat "acesta" cat si "celalalt"- valoare de adevar
acesta = True
celalalt = True
print("acesta and celalalt: ", acesta and celalalt) #True and True
celalalt = False
print("acesta and celalalt: ", acesta and celalalt) # True and False
acesta= False
print("acesta and celalalt: ", acesta and celalalt) # False and False
celalalt= True
print("acesta and celalalt: ", acesta and celalalt) # False and true

print("-"*40)

# Operatorul "or" - SAU
#Fie alpha, fie beta - valoare de adevar (oricare din ele)

alpha, beta = True, True
print("alpha or beta: ", alpha or beta) #True or True
alpha, beta = True, False
print("alpha or beta: ", alpha or beta) #True or False
alpha, beta = False, False
print("alpha or beta: ", alpha or beta) #False or False
alpha, beta = False, True
print("alpha or beta: ", alpha or beta) #False or True

#operatori logici
# and: Acest operator returnează True dacă ambele condiții evaluate sunt adevărate.
# Altfel, returnează False.
#

x = 5
print(x > 3 and x < 10) # Outputs True


# or: Acest operator returnează True dacă cel puțin
# una dintre condițiile evaluate este adevărată. Altfel, returnează False.

x = 5
print(x > 3 or x > 10) # Outputs True


# not: Acest operator neghează rezultatul condiției pe care o evaluează.
# Dacă condiția este adevărată, not va returna False și viceversa.

x = 5
print(not(x > 3 and x < 10)) # Outputs False