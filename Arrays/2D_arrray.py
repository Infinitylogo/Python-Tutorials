#Created By Ritu Raj

import numpy as np

# twoDArray = np.array([[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]])


#insert in twoDArray>>>

# twoDArray_insert = np.insert(twoDArray, 2, [[17,18,19,20]], axis = 1)  #(O(m*n))
# print(twoDArray_insert)


# append>>>
# twoDArray_append = np.append(twoDArray, [[17,18,19,20]], axis = 0)  #(O(m*n)) # row wise 
# print(twoDArray_append)

# acessing >>> O(1)

# print(twoDArray[3][3]) >> O(1) and O(1)

# print(len(twoDArray)) # >>> len of columns

# print(len(twoDArray[0])) 

# def accessing_elements(array, row, col):
#     if row >=len(array) or col >= len(array[0]):
#         return f"value is not present"
#     else:
#         return array[row][col]

# print(accessing_elements(twoDArray, 2, 3))


# searching >>>  O(m*n)    --- O(m*n)  and space complexity will be O(1)

# def target_value(array, tar):
#     for i in range(len(array)):  #---m 
#         for j in range(len(array[0])): #---n
#             if array[i][j] == tar: # O(1)
#                 return f"tar is at postion row {i} col - {j}" #--O(1)
#     else:
#         return "it is not present"
    
# print(target_value(twoDArray, 12))


##  Deletion >>> O(m*n) , O(m*n)

# delt = np.delete(twoDArray, 0, axis=0)
# print(delt)

# threeDArray = np.array([[[1,2,3,4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15,16]]])
# print(threeDArray)


# list and arrays>>

# 3d arrays>>>>>>>>>>>>>

# import pprint
 
# def ThreeD(a, b, c):
#     lst = [[ ['3' for col in range(a)] for col in range(b)] for row in range(c)]
#     return lst


# # Driver Code
# # col1 = 5
# # col2 = 3
# # row = 2
# # used the pretty printed function
# pprint.pprint(ThreeD(5, 3, 2))

# print(np.zeros((2,3,2)))

#  1-D to 2-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)


# #  1-D to 3-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)


# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

