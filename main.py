import numpy as np


# THIS IS FOR A DEMO
# creating a copy
# arr = np.array([2,3,4,5,6])
#
# rev_arr = np.array(arr[::-1])
#
# rev_arr[0] = 100
#
# print(" orginal arr :" , arr)
#
# print(" reversed arr : ", rev_arr)


# creating a view
arr = np.array([2,3,4,5,6])

rev_arr = arr[::-1]

rev_arr[0] = 100

print(" orginal arr :" , arr)

print(" reversed arr : ", rev_arr)