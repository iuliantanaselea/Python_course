ske = ('-' * 44)
print(ske)

"""
Context Manager = Un concept care ne permite sa gestionam accesul la diverse resurse prin apelarea
                automata a doua functii la intrarea si iesirea din context
    ! in Python, 'context managerul' este dat de clauza 'with'
Sintaxa: 
    with Context_manager() as variabila:
        # fa ceva cu variabila care rezulta din Context_manager
    # Aici nu vom mai avea acces la variabila deoarece s-a inchis aceasta resursa
"""
with open('test_file.txt', 'r') as f:  # 'r' = read
    print(f.readlines())
# print(f.readlines()) # fisierul a fost inchis in acest punct, nu mai avem acces la el
# ValueError: I/O operation on closed file

print(ske)

"""
Ca sa definim propriul nostru context_manager, avem nevoie de o clasa care implementeaza 
functiile '__enter__' si '__exit__'.
"""


class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file  # ce se returneaza aici se poate stoca intr-o variabila folosind 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('test_file.txt', 'r') as f:
    print(f.readlines())

print(ske)


class HelloContextManager:
    def __enter__(self):
        print('Entering the context')
        return 'Hello World'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving the context')
        if exc_type == IndexError:
            print(f'Exception type: {exc_type}')
            print(f'Exception message: {exc_val}')
        return True  # pentru ca am returnat 'True' nu se propaga exceptia in afara contextului
        # la return 'False' sau o, exceptia merge mai departe in afara contextului


with HelloContextManager() as hello:
    print(hello)
    hello[100]

print(ske)

from contextlib import contextmanager


@contextmanager
def file_manager(file_name, mode):
    f = open(file_name, mode)  # exact la fel ca FileManager (clasa de mai sus)
    yield f
    f.close()


with file_manager('test_file.txt', 'r') as f:
    print(f.readlines())
   