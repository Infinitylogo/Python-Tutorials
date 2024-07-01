# Ritu Raj

# Binary Search -- for sorted arrays
# time complexity is  :-- best case O(1), average and worst case :-- log(n)
# space complexity is :-- O(1)


def binarySearch(array, target):
    if len(array)==0:
        return -1
    
    start = 0
    end = len(array)-1

    mid = start + (end-start)//2
    while not(array[mid]==target) and start<=end:
        if array[mid]>target:
            end = mid-1
        else:
            start = mid+1
            
        mid = start + (end-start)//2
    return mid if array[mid] == target else -1

print(binarySearch([1,2,3,4,5,6,7], 8))