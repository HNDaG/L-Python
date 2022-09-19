import numpy as np

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # int32

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)# <U6

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)      # [b'1' b'2' b'3' b'4']
print(arr.dtype)# |S1

# For i, u, f, S and U we can define size
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)# [1, 2, 3, 4]
print(arr.dtype) # int32

print("Converting data types")
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)#  here is the diff
print(newarr)
print(newarr.dtype)

#bool
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)