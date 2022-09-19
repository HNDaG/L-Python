import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

'''
The copy SHOULD NOT be affected by the changes made to the original array.

The view SHOULD be affected by the changes made to the original array.
The original array SHOULD be affected by the changes made to the view.
'''