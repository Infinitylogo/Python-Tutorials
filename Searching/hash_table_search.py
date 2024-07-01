# Ritu Raj

def hash_table_solu(array, target):
    hash_table = {value:index for index, value in enumerate(array)}
    return hash_table.get(target, -1)

# it can be performed on unsorted arrays

#average case :-- O(1) and worst case O(n)
#space complexity --- O(n)

print(hash_table_solu([6,7,1,2,3,4,5], 6))