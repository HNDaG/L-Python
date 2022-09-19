'''
>>> # Unpacking strings
>>> a, b, c = '123'
>>> a
'1'
>>> b
'2'
>>> c
'3'
>>> # Unpacking lists
>>> a, b, c = [1, 2, 3]
>>> a
1
>>> b
2
>>> c
3
>>> # Unpacking generators
>>> gen = (i ** 2 for i in range(3))
>>> a, b, c = gen
>>> a
0
>>> b
1
>>> c
4
>>> # Unpacking dictionaries (keys, values, and items)
>>> my_dict = {'one': 1, 'two':2, 'three': 3}
>>> a, b, c = my_dict  # Unpack keys
>>> a
'one'
>>> b
'two'
>>> c
'three'
>>> a, b, c = my_dict.values()  # Unpack values
>>> a
1
>>> b
2
>>> c
3
>>> a, b, c = my_dict.items()  # Unpacking key-value pairs
>>> a
('one', 1)
>>> b
('two', 2)
>>> c
('three', 3)

'''

my_dict = {'one': 1, 'two':2, 'three': 3}
a, b, c = my_dict.items()  # Unpack keys
print(type(a), b, c)


'''

>>> *a, = 1, 2
>>> a
[1, 2]

'''


gen = (2 ** x for x in range(10))
print(gen)#
*g, = gen  # coma is needed
print(g)

#
def f(): 
   return 1,2,3 

def g(): 
   return 1,2

def h(): 
   return 1,2,3,4


x,y,*_ = g()                                                                                                                  
print(_)                                                                                                                      
x,y,*_ = h()                                                                                                                  
print(_) 