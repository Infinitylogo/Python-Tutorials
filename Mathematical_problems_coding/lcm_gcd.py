# lcm  = a*b  // GCD(a, b)
# GCD = a , b = b, a%b


def gcd(a,b):
    while b:
        a, b  = b, a%b
    return a

# print(gcd(48,18))

def lcm(a,b):
    return (a*b)//gcd(a,b)

# print(lcm(48,18))


# multiple numbers:--

from functools import reduce

### build in library for python : -- pandas, numpy, sum()


def gcd_mul(num):
    return reduce(gcd,num)

def lcm_mul(num):
    return reduce(lcm,num)

print(lcm_mul([48,18,30]))


