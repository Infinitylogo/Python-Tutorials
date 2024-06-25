### 2 **6
## 2**10 === 1mb==1024kb

# add, sub, mul ad div
# ascii codes -- a === 97 and A = 65

# tools pandas, numpy, excel sheet, pyspark,   
# big data sql or no sql -- MySQL, MongoDB

# import pdb

# postive number

def power_gen_pos(num, expo):
    res = 1 # base 
    while expo > 0:
        if expo%2 ==1:
            res *= num
        num *=num
        expo //=2
    return res

# logn

# print(power_gen(10, 5))

# print(pow(10, -5))

def power_gen_for_pos_nagative_number(num, expo):
    if expo ==0:
        return 1
    
    if expo < 0:
        num = 1/num
        expo = -expo

    res = 1 # base 
    while expo > 0:
        if expo%2 ==1:
            res *= num
        num *=num
        expo //=2
    return res

# print(power_gen_for_pos_nagative_number(2,-2))

def power_(num, expo):
    return num**expo





