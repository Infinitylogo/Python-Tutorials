# Ritu Raj

# 12 :-- 1,2,3,4,6,12

import math

def factors_(n):
    factor = []

    for i in range(1, int(math.sqrt(n))+1):
        if n%i ==0:
            factor.append(i)
            if i != n//i:
                factor.append(n//i)
    factor.sort()
    return factor

print(factors_(100)) # [1, 2, 4, 5, 10, 20, 25, 50, 100]
