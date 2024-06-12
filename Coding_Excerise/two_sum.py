# two sum problems:--
nums = [2, 7, 11, 15]
target = 9

def two_pair_problem(nums, target):
    seen_dict ={}
    for i, num  in enumerate(nums):
        complement = target - num
        if complement in seen_dict:
             return [seen_dict[complement], i]

        seen_dict[num] = i

print(two_pair_problem(nums, target))