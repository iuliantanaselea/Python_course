

# STRING SLICING

import string

alphabet = string.ascii_lowercase       #   'abcdefghijklmnopqrstuvwxyz'

print(alphabet)

'''
String slicing se refera la faptul ca eu pot desprinde bucati dintr-un string (lista)
si sa le operam separat 
'''

# Operatiune slice end

substring = alphabet[:3]            # :3    - index
print(f"substring: {substring}")


# Slice functioneaza asa : [start:end:step]
substring2 = alphabet[1:3]
print(f" substring2: {substring2}")


# Slice cu stepping     , adica din cat in cat

substring_step = alphabet[0:20:2]
print(substring_step)       # indecsii impari

#indecsi pari
substring_step2 = alphabet[1:21:2]
print(substring_step2)       #indecsi pari



from inspect import currentframe, getframeinfo

cf = currentframe()
filename = getframeinfo(cf).filename

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

print( "This is line , python says line ", get_linenumber())
print( "The filename is ", get_linenumber())