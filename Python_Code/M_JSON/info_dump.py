'''
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

Python has a built-in package called json, which can be used to work with JSON data.
'''

import json


    # If you have a JSON string, you can parse it by using the json.loads() method.
    # The result will be a Python dictionary.

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
del x, y


    #Convert from Python to JSON
    #If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print("dict -> JSON", y)
del x, y


# cAN be converted
print("1  ", json.dumps({"name": "John", "age": 30}))
print("2  ",json.dumps(["apple", "bananas"]))
print("3  ",json.dumps(("apple", "bananas")))
print("4  ",json.dumps("hello"))
print("5  ",json.dumps(42))
print("6  ",json.dumps(31.76))
print("7  ",json.dumps(True))
print("8  ",json.dumps(False))
print("9  ",json.dumps(None))

'''
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
'''

# Convert a Python object containing all the legal data types:


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print("All legal data types -> ", json.dumps(x))

# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

json.dumps(x, indent=4)

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)
# Or even alphabetic sort

z = json.dumps(x, indent=4, sort_keys=True)
print("\n\n\n", z)