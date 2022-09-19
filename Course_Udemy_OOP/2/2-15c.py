class Person:
    def say_hello():
        print("Hello")

print(type(Person.say_hello))

p = Person()

print(hex(id(p)))
print(type(p.say_hello)) # not fun but method

                
class person:
    def say_hello(*args):
       print ("HGello args: ", args)

P = person()
P.say_hello((1, 4, 3,2, 1))

class Person3:
    def say_hello(self):
        print(self)

p3 = Person3()

print(p3.__dict__)

m_hello = P.say_hello
m_hello("func copy")

print(hex(id(P)))#   These two is basicly the same adres
print(m_hello.__self__)


class Person4:
    def say_hello(self):
        print(f'instance method called from {self}')

p4 = Person4()

print(hex(id(p4)))
p4.say_hello()

Person4.do_work = lambda self: f'do_aork called from {self}'

print(Person4.__dict__)
