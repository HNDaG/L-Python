#Add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print("---1---")
print(thisset)

#Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print("---2---")
print(thisset)

#Add.... sets?
#Add Any Iterable
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print("---3---")
print(thisset)


#Remove item
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
#Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
thisset.discard("banana")
#Note: If the item to remove does not exist, discard() will NOT raise an error.
print("---4---")
print(thisset)

#   .pop() will remove random element and return it as a return value



#clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("---5---")
print(thisset)


thisset = {"apple", "banana", "cherry"}

print("---6---")
print(thisset)



'''
All methods
https://www.w3schools.com/python/python_sets_methods.asp

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''