class person:
    age = 30
    def print_age(self):
        print(self.age)

p= person()
p.print_age()
p.age = 28
p.print_age()
print(person.age)