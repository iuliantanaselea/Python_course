"""
Exercitii recapitulative
"""


# Exercitiul 1
"""
1. Crează o functie Python care inversează și returnează un număr întreg pozitiv. În cazul unui număr negativ, afișează o eroare.
Exemple:
reverse(1234567) => 7654321
reverse(10) => 1
reverse(101) => 101
reverse(10000000) => 1
reverse(-65) => eroare
"""


# Varianta 1
def reverse_number(number):
    if number < 0:
        raise Exception("Error, number is negative")
    else:
        invers = int(str(number)[::-1])
        return invers


x = reverse_number(33214)
print(x)


# Varianta 2

def reverse(n):
    if n < 0:
        return "eroare"
    n_list = list(str(n))
    n_list.reverse()
    return int(''.join(n_list))


x = reverse(33214)
print(x)
# Exercitiul 2
"""
2. Creaza o functie Python care primește o lista și un număr întreg pozitiv k, si roteste lista
cu k pozitii.
Exemple:
rotate([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], 4) => [5, 1, 2, 3, 4]
rotate([1, 2, 3, 4, 5], 8) => [4, 5, 1, 2, 3]
"""


def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]


result = rotate([1, 2, 3, 4, 5], 2)
print(result)

# Exercitiul 3
"""
3. Creaza o functie Python care primește 2 stringuri, și verifica dacă acestea sunt anagrame (case-insensitive).
Exemple:
is_anagram(‘Adela’, ‘ealad’) => True
is_anagram(‘ITFactory’, ‘acfiorty’) => True
is_anagram(‘Stringy’, ‘gringsty’) => False
is_anagram(‘ana’, ‘ioana’) => False
"""


def is_anagram(string_1, string_2):
    st_1 = str(sorted(string_1)).lower()
    st_2 = str(sorted(string_2)).lower()
    if st_1 == st_2:
        print(f'{string_1} , {string_2} => True')
    else:
        print(f'{string_1} , {string_2} => False')


is_anagram('Adela', 'ealad')
is_anagram('ITFactory', 'acfiorty')

# Exercitiul 4
"""
4. Creaza o functie Python care primește o lista de numere, si il returneaza pe al doilea cel
mai mare numar distinct.
Exemple:
get_second_biggest([1,2,3,4,5]) => 4
get_second_biggest([1,2,3,4,4]) => 3
get_second_biggest([1,2,4,4,4]) => 2
get_second_biggest([-1,-2,-3,-4,-5]) => -2
"""


def get_second_biggest(numbers):
    if len(numbers) < 2:
        raise ValueError("Nu exista suficiente numere in lista")
    distinct_numbers = set(numbers)
    result = sorted(distinct_numbers)[-2]
    return result


print(get_second_biggest([1, 2, 3, 4, 5]))

# Exercitiul 5
"""
5. Creaza o functie Python care primeste doua stringuri ce reprezinta niste numere foarte mari,
si returneaza rezultatul adunarii “numerelor”, tot sub format string:
Exemple:
add_two(‘12345’, ‘12345’) => ‘24690’
add_two(‘1234’, ‘4321’) => ‘5555’
add_two(‘563895634’, ‘548967348053’) => ‘549531243687’
"""


def add_two(s1, s2):
    return f'(`{s1}` , `{s2}`) => {str(int(s1) + int(s2))}'


print(add_two('563895634', '548967348053'))
# Exercitiul 6
"""
6. Creaza o functie Python care primeste un numar n, si o lista de numere de dimensiune n-1. 
In lista se afla toate numerele de la 1 la n, in afara de 1. Functia trebuie sa gaseasca 
acel numar in cel mai eficient mod posibil si sa-l returneze.
Exemple:
find_missing(5, [1,2,3,5]) => 4
find_missing(2, [1]) => 2
find_missing(7, [6,5,1,3,2,7]) => 4
"""


def find_missing2(n, l_n):
    suma_totala = (n * (n + 1)) // 2
    suma_lista = sum(l_n)
    numar_lipsa = suma_totala - suma_lista
    return f'({n} {l_n} => {numar_lipsa}'


print(find_missing2(5, [1, 2, 3, 5]))

# Exercitiul 7
"""
7. Creaza o clasa Calendar, care primeste ca unic parametru un an, si genereaza “calendarul” acelui an. Se va tine cont de faptul daca anul este bisect sau nu. Metode:
-> init(an)
-> print_calendar(luna) - va printa calendarul pentru luna menționată intr-un format user-friendly, ex
October 2022
Mo 	Tu 	We 	Th 	Fr 	Sa 	Su
1 	2
3 	4 	5 	6 	7 	8 	9
10 	11 	12 	13 	14 	15 	16
17 	18 	19 	20 	21 	22 	23
24 	25 	26 	27 	28 	29 	30
31
	-> get_day_of_week(zi, luna) - va returna ce zi din saptamna este, exemplu ‘Marti’
-> get_days_in_month(luna) - va returna numarul de zile din luna respectivă;
"""

import datetime
class Calendar():
    def __init__(self, an):
        self.an = an

    def an_bisect(self):
        return datetime.date(self.year, 12, 31).strftime('%j') == '366'

    def get_days_of_month(self, month):
        if month in [4, 5, 9, 11]:
            return 30
        elif month == 2:
            if self.an_bisect():
                return 29
            else:
                return 28
        else:
            return 31

    def get_calendar_month(self, month):
        name_month = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        print(name_month[month - 1], self.an)
        for name in day_names:
            print(name, end='\t')
        print()
        first_day = datetime.date(self.an, month, 1).weekday()
        print()
        for _ in range(first_day):
            print('\t', end='')
        days_in_month = self.get_days_of_month(month)
        for day in range(1, days_in_month+1):
            print(day, end='\t')
            if (first_day + day) %7 == 0:
                print()
        print()

    def get_days_in_month(self,month, day):
        day_of_month =datetime.date(self.an, month,day).strftime("%A")
        return day_of_month

calendar = Calendar(2023)
calendar.get_calendar_month(9)
print(calendar.get_days_in_month(9,21))