'''
Modify Object Properties
You can modify properties on objects like this:

Example
Set the age of p1 to 40:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " I'm " + str(self.age) )

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
p1.myfunc()

del p1.age
#p1.myfunc() error 

del p1

class Game:
  pass

print(type(Game))