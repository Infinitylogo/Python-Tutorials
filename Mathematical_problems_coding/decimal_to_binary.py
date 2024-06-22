# 10 :-- 
# 2**2, 2**1, 2**0

# 16,8,4,2,1
# 0  1 1 0 1
# 1  0 0 1 1

def cover_bin(num):
    return bin(num)[2:]
# print(cover_bin(10))

def math_terms_b_to_d(num):
    if num==0:
        return '0'
    
    bina= []
    while num>0:
        bina.append(str(num%2))
        num//=2
    bina.reverse()
    return ''.join(bina)

print(math_terms_b_to_d(13))
print(math_terms_b_to_d(19))


