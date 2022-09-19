from functools import wraps

def h1(func):
    
    @wraps(func) # for savin documentetion, because name and __doc__ will be lost 
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("<\h1>")
    return inner



def hello1(name, surname):
    '''
    printing hello name surname
    '''
    print(f"Hello {name} {surname}, it's nice to meet you!")

@h1          # Anoother way of usin wrap ref to   hello1 = h1(hello1)
def hello2(name, surname):
    '''
    printing hello name surname
    '''
    print(f"Hello {name} {surname}, it's nice to meet you!")



hello1 = h1(hello1)
hello1("Nik1", "Hohulia")
print(hello1.__doc__)

hello2("Nik2", "Hohulia")