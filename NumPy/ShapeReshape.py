import numpy as np

#  The shape of an array is the number of elements in each dimension.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)#  (2, 4)


arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(arr)
print(newarr)

# unknown value can be specifyed as -1 and np will calculete it itself
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

'''
Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, 
ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. 
These fall under Intermediate to Advanced section of numpy.
'''