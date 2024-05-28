# @created by Ritu Raj

#time com :-- O(n) and O(1)
list_com = [1, 2, 3, 4, 5]

# applying list comprehension
new_list = [ item*2 for item in list_com]

print(new_list)  # [2, 4, 6, 8, 10]

string = 'python'
updated_list  = [item  for item in string] 
print(updated_list) # ['p', 'y', 't', 'h', 'o', 'n']
print('using list directly')
print(list(string))

number_list = [1,2, 3, 4, 5,-3,-4, -5,-6, 23, -29]
# conditonal list comprehension

positive_list = [i for i in number_list if i > 0] 
print(positive_list) #[1, 2, 3, 4, 5, 23] (postive elements form list)  


# checking consonants
def con(letter):
    v= 'aeiou'
    return letter.isalpha() and letter.lower() not in v

print(con('a'))
print(con('z'))

#using list comprehension
sentence ='lets code'
cons = [i for i in sentence if con(i)]
print(cons)

# functions inside list comprehension
def check_post_num(n):
    return n if n>0 else "negative number"

number_list_updated = [check_post_num(i) for i in number_list]
print(number_list_updated)

# [i for i in range(5)] # refactorization


# print([i for i in range(5)])
# # a =[]
# # for i in range(5):
# #     a.append(i)

# # print(a)