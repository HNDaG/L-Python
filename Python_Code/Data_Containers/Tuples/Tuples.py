'''
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:
'''





mytuple = ("apple", "banana", "cherry")
print("--1--")
print(len(mytuple))

#One item tuple, remember the comma:
thistuple = ("apple",)
print("--2--")
print(type(thistuple))

#adding and removing from tuples is basicly to convert them to lists using list method
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("--3--")
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("--4--")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print("--5--")
print(thistuple)
del thistuple

print("--6--")
print(mytuple*3)
