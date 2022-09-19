i = 1
while i < 6:
  print(i)
  i += 1

#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#FOR LOOP

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break#loop stopped here
  print(x)

#The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)
#The range() function defaults to 0 as a starting value, however it is possible to 
# specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 30, 3):
  print(x)



list3 = list(range(10))
#else
for x in range(len(list3)):
  print(x)
else:
  print("Finally finished!")
  #Note: The else block will NOT be executed if the loop is stopped by a break statement.
