# Created by Ritu Raj
#         0 1 2 3 4 
list = [1,2,3 ,5,"1", 12.90, [1, 2, 3], [5, 6, 7]]
#                       -3        -2            -1


# traversing >>
# o(n) , O(1)
for i in list:
    print(i, end=" ")

print()

for i in range(len(list)):
    print(list[i], end= " ")

print()

#accessing 

print(list[2]) # O(1), and O(1)

# update
list[2] = 33 # o(1), O(1)
print(list)


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
b = []
for i in a:
    if isinstance(i, list):
        b.extend(i)
    else:
        b.append(i)

print(b)

