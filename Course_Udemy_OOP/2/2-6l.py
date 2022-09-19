class Person:
    age = 30
    pass

print(type(Person()))
print(Person.__class__)

p = Person()
print(isinstance(p, Person))


print(getattr(Person, 'age'))# return value if attr not exist -> exception
print(getattr(Person, 'ageee', "default"))

setattr(Person, "age", "19")
print(Person.age, p.age)

setattr(Person, 'Name', "Nik")
Person.Surname = "Hoh"
print(Person.Name, Person.Surname)
print(p.Name, p.Surname)

print(Person.__dict__) # returnmapping proxi -> read only dic


delattr(Person, "age")
# del Person.age
print(Person.__dict__)





