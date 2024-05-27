# @created by Ritu Raj

#time com :-- O(n) and O(1)
list_com = [1, 2, 3, 4, 5]

# applying list comprehension
new_list = [ item*2 for item in list_com]

print(new_list)  # [2, 4, 6, 8, 10]

string = 'python'
updated_list  = [ item  for item in string] 
print(updated_list) # ['p', 'y', 't', 'h', 'o', 'n']

number_list = [1,2, 3, 4, 5,-3,-4, -5,-6, 23, -29]
# conditonal list comprehension

positive_list = [i for i in number_list if i >0] 
print(positive_list) #[1, 2, 3, 4, 5, 23] (postive elements form list)  