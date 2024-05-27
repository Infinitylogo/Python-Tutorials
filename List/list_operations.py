# Created by Ritu Raj
#         0 1 2 3 4 
list1 = [1,2,3 ,5,"1", 12.90, [1, 2, 3], [5, 6, 7]]
#                       -3        -2            -1


# traversing >>
# o(n) , O(1)
for i in list1:
    print(i, end=" ")

print()

for i in range(len(list1)):
    print(list1[i], end= " ")

print()

#accessing 

print(list1[2]) # O(1), and O(1)

# update
list1[2] = 33 # o(1), O(1)
print(list1)


# Insertion  :-- insert (n), 1, append 1, 1, extend n, n

a = [1,2,3,4,5]
a.insert(0, 11) # docs.python.org
print(a)

a.append(12)
print(a)

b = [1, 2,3 ,4]
a.extend(b)
print(a)

a = [1,2,3,4, [1,2], [4,5]]
c = []
for i in a:
    if isinstance(i, list):
        c.extend(i)
    else:
        c.append(i)

print(c)

#difference between list and arrays
import numpy as np

print('Array and Lists')
array_same_dtype = np.array([1, 2, 3,4, 5])
list_any_dtype = [1, 2, 'a', 3, '3']

print(array_same_dtype,list_any_dtype)
print(array_same_dtype/2) # arithematic operations

trying_to_create_array_with_diff_dtype = np.array([1, 2, 3,4, 5, 'a'])
print(array_same_dtype)
