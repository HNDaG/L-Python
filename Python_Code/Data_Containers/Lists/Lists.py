
from tokenize import maybe


mylist = ["apple", "banana", "cherry"]

mylist.append('bread')
mylist.append('potatoes')
mylist.copy()
#1
print(mylist[2:4])
#2
print(mylist[-1])

#print(mylist[-6]) Index out of range

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
#3
print(thislist)
thislist.insert(2, "Inserted")
#4
print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist[1:3] = ["watermelon"]          -> [Apple , Watermelon]

#extend()
mylist.extend(thislist)
#5
print(mylist)
#6
print(thislist)


#del
thislistA = ["apple", "banana", "cherry"]
del thislistA[0]
print(thislist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
#7
print(newlist)
del fruits
del newlist



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
#8
print(newlist)

#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)# or just () if not reversed
#9
print(thislist)


#sort using key
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
#10
print(thislist)

#Upper and lower case letters are different
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
#11
print(thislist)


#Copying lists like list1=list2 will be a reference. copy() shoud be used
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
#12
print(mylist)


#Joining list using list1 = list2 + list3 OR loop +append OR .extend()


#The reverse() method reverses the current sorting order of the elements.



'''
Looping throught lists 



thislist = ["apple", "banana", "cherry"]
for x in thislist:
      print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


'''






'''
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
'''
type()
From Python's perspective, lists are defined as objects with the data type 'list':
<class 'list'>

A list can contain different data types:

Example
A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

he list() Constructor
It is also possible to use the list() constructor when creating a new list.
Example
Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

'''