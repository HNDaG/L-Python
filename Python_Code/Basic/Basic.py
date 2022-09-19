# Test program
"""
Comment example
"""

import random


# Initialization
A = "Joan"
a = 'Bear'
g = float(2)

xx, yy, zz = "Orange", "Banana", "Cherry"
xxx = yyy = zzz = "Orange"

print(A, a, g)

# List example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)


# Numbers

x = 1    # int
y = 2.8  # float
z = 3+1j   # complex
# x = 35e3 => 35000

aa = float(x)
bb = int(y)
cc = complex(y)

print(aa)
print(bb)
print(cc)

print(type(aa))
print(type(bb))
print(type(cc))

# Random
'''
import random
print(random.randrange(1, 10))
'''
print(random.randrange(1, 10))

# String 
'''

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
'''
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

s = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""



