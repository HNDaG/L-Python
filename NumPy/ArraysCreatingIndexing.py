import numpy as np



array0 = np.array(5)
array1 = np.array(range(1,5))
array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("Print arrays")
print(array0)
print(array1)
print(array2)

print("Indexing")
print(array1[2])
print(array2[1][-2:])# [7, 8]
print(array2[1, -2:])# [7, 8]
print(array2[0, 2])  # 3

print("Dimentions")
array3 = np.array([
    [[1, 2, 3], [4, 5, 6]], 
    [[7, 8, 9], [10, 11, 12]]
    ])
print(array3)
print(array3.ndim)
print(array3[1][0][1])


print("Fout dimentions")
array4 = np.array([1, 2, 3, 4, 5], ndmin=5)
print("Array4 \n", array4)
print(array4[0][0][0][0][2])

print("Slicing")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
del arr

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::3])
print(arr[::2])#:Return every other element from the entire array:
print(arr[::1])
del arr

print("Slicing step")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])


print(tuple(range(0, 100, 5)))


