fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print("--1--")
print(green)
print(yellow)
print(red)


#Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print("--2--")
print(green)
print(yellow)
print(red)


#Or even

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
print("--3--")
print(green)
print(tropic)
print(red)