# Ritu Raj

# Linear Search or sequential search 

# time complexity is o(N) and sc is O(1)

def linearSearch(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return f"index is {i} and value is {array[i]}"
    return -1

print(linearSearch([1,2,3,7,5,67,9], 67))
print(linearSearch([1,2,3,7,5,67,9], 0))