from msilib import type_binary


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
print(type(x))

#########################

#Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    pass
    #add properties etc.
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
# and we are ready to add functionality in the __init__() function.