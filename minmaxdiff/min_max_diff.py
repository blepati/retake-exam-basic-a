# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases
nums = [5, 7, 9, 15, 22]

def min_max_diff(nums):
    if nums == [ ]:
        return 0
    if len(nums) == 1:
        return 0
    max_num = 0
    min_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    for num in nums:
        if min_num > num:
            min_num = num
    return max_num - min_num

print(min_max_diff(nums))
