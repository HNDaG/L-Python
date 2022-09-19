#Efficient multi-dimensional iterator object to iterate over arrays. 

import numpy as np


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:  #   While using only one for will return lists [...]
  for y in x:
    for z in y:
      print(z)

print("\nnp.nditer\n")
for x in np.nditer(arr):
  print(x)


'''
Iterating Array With Different Data Types
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

Iterate through the array as a string:
'''
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


#Iterate through every scalar element of the 2D array skipping 1 element:

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)


# For getting elements index
print("For getting elements index")
  
