# power set
# [1,2,3] = [[],[1],[2],[3],[1,2], [1,3], [2,3], [1,2,3]]

def create_power_set(num):
    subset =[[]]
    for i in num:
        subset += [j+[i] for j in subset]

    return subset

print(create_power_set([1,2,3]))

# factorial, prime, arstring nu, palindrome 
