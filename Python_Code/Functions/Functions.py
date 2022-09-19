def my_function():
  print("Hello from a function")

my_function()

#With arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#The prametrs order cam be manually specified
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

#This way the function will receive a dictionary of arguments, and can access the items accordingly:

#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])
  print(kid)

my_function(fname = "Tobias", lname = "Refsnes")

#Defult 
def my_function(country = "Norway"):
  print("I am from " + country)


#Pssing list into the function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


#there it is also return and pass keyword? and their use is pretty ovious
def my_function(x):
  return 5 * x