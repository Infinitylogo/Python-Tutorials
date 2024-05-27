# Omega, theta, and big O

#>>>>>>>>>>>>>>>>...
#time complexity >>>>>>>>>>>>>>>>>
"""
# Omega, theta, and big O

[1,2,3,4,5,6] ----

insert at 0 :--  Omega  O(1) >>> best complexity 
insert at last place anywhere in that list :-- Average cases (O(N)) -- O(1) (theta)
insert at middle of the list:-- worst case scenerio ( O(N) ) ( big O)


O(1):-- constant time 
O(N) :-- linear time
O(N**2) :-- quadratic complexity 
O(log(n)) :-- logirithm(n)

"""


""" O(1)"""
# a= 1
# b=2
# print(a+b) #>>>>>>>>>>>>>>O(1)

# lis = [1, 2, 3, 4]
# for i in range(0, len(lis)): #>>>> O(n)
#     print(i) 


# def get(lis):
#     for i in range(0, len(lis)): #>>>> O(n)
#         print(i) 

#     for i in range(0, len(lis)): #>>>> O(n)
#         print(i) 

# get(lis) #  >>> O(n+n) >>O(2n) >>> O(n)


# def get(a, b):
#     for i in range(0, a): #>>>> O(a)
#         print(i) 

#     for i in range(0, b): #>>>> O(b)
#         print(i) 

# get(a=4, b=5) #  >>> O(a+b) 

def get(n=5):
    for i in range(0, n): #>>>> O(n)  >> (O(n**2))
        for j in range(0, n): #>>> O(n)
            print(i,j)

get(n=5)

def get(n=5, m=6):
    for i in range(0, n): #>>>> O(n)  >> (O(n*m))
        for j in range(0, m): #>>> O(n)
            print(i,j)

get(n=5, m=6)


#log(n) >>>> divide and conquer 
# [1,2,3,4,5,6] == 0+
#  [4, 5, 6]== [4] [5, 6]
# n//2 


# lis = [1, 2, 3, 4, 5] >> O(n) , O(logn), 

# log(200000000) base 2 =18


#space complexity >>>


a = 5  # O(1)



def addi(n):
    if n<3:
        return 1
    return n+addi(n)

# Space complexity :-- O(n)


def sum_count(sum1, i):
    sum1 = sum1+i
    return sum1
    
sum1 =0   #oeeeff567 
for i in range(0,5): 
    sum1 = sum_count(sum1, i)

# time complexity :-- O(n)
# Space complexity :-- O(1)


# END

# three pot 

# a = 10 # >> O(1) 

# [1,2,4,6] >>>  O(n)