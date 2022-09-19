#

"""
That's where the Python built-in functions any() and all() come in. any() 

iterates through every item in an object and returns True if any item is 

equal to True. all() goes through every item in an object and returns True 

only if every item in the object is equal to True.

"""

arr = [0, 0, 0]

print("arr[0, 0, 0]  ",any(arr))

race_wins_indy_500 = [False, False, True, False]
print("arr  ",any(race_wins_indy_500))


indy_500_2018_john = {
	'driver_name': 'John Appleseed',
	'race_year': 2018,
	'top_ten': True
}
print("dict  ", any(indy_500_2018_john))

top_10_ranking = "" # false bercause is empty
print("s  ",any(top_10_ranking))


#ALL 
'''
all() is a built-in Python function that returns True when all items in an iterable object are True, and returns False otherwise. 

In addition, if the iterable object is empty, the all() method will return True.


all() returns True when:

All values are equal to True
The iterable object is empty
Otherwise, all() returns False.
'''
print("ALL()")
race_wins_indy_500 = [False, False, True, False]
print("arr  ",all(race_wins_indy_500))

indy_500_2018_john = {
	'driver_name': 'John Appleseed',
	'race_year': 2018,
	'top_ten': True
}
print("dict  ",any(indy_500_2018_john))


racer_name = "John Appleseed"
print("s  ", all(racer_name))