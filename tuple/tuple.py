# immutable 
# time space O(1), O(N)
tup = 1,2,3,4,5,5
# print(tup)

tup2 = (1,2,3,4,5,6)
# print(tup2)

tup = 1,2,3
# print(tup)

# traverse, search , count, index

# for i in tup:
#     print(i, end=" ")

# # print("")
# tar = 3
# for i in range(len(tup)):
#     if tup[i] == tar:
#         print(i)

# # print(tup.index(3))

# print(tup.count(3)) 



# tuple_com = (i for i in range(5))
# print(list(tuple_com))


# value = [(1, 2), (2, 3), (3,4)]

# for i in value:
#     print(i)
#     key, val = i
#     print(val, key)





# Class and method



# list questions :--
new_list = [12,35,9,56,24]
# temp = new_list[0]
# new_list[0] = new_list[len(new_list)-1]
# new_list[len(new_list)-1] = temp

# print(new_list)


new_list[-1], new_list[len(new_list)//2] = new_list[len(new_list)//2], new_list[-1]
print(new_list)
