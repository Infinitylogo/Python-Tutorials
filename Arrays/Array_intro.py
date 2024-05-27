# Created By Ritu Raj


# array or numpy   >>> pip3 install numpy
import array

# empty array>>>
array_1 = array.array('i') # O(1)
print(array_1)

# # array with some elements>>
# array_2 = array.array('i', [1, 2, 3, 4, 5]) # O(N)
# print(array_2)

# # how we can create array using numpy 
# import numpy as np
# nump_arr = np.array([], dtype='int')
# print(nump_arr)
# nump_arr1 = np.array([1,2,2,3,4,5], dtype='int')
# print(nump_arr1)



# one dim, two dim and three dim

# [[1, 2, 3], [4,5, 6], [7, 8, 9]]

two_dim = [array.array('i', [1, 2, 3]), array.array('i', [4, 5, 6]), array.array('i',[7, 8, 9])]
print(two_dim)
print(two_dim[0][0])
print(two_dim[1][1])
print(two_dim[2][2])


# [     0  1  2
#   0   1, 2, 3
#   1   4, 5, 6
#   2   7, 8, 9
# ]